import logging
from turkish_suffix_library.turkish import Turkish
import re
import io
import pprint

from nltk.translate.bleu_score import SmoothingFunction
from nltk.translate import bleu

logging.getLogger('transformers').setLevel(logging.WARNING)
log = logging.getLogger(__name__)

import time
import math

import torch
from torch import optim, nn, cuda
from transformers import AdamW, BertTokenizer
from torch.utils.data import DataLoader
from transformers import BertModel

from config import checkpoint, bert_path, mb, dl_workers, device, bert_hidden_size, decoder_hidden_size, \
    bert_vocab_size, decoder_input_size, dropout, epochs, clip, model_path, bert_model, encoder_trained, \
    attention_hidden_size, num_layers, weight_decay, betas, lr, momentum
from model.utils import load_checkpoint, init_weights, save_checkpoint, enable_reproducibility, model_size, no_grad
from model import Attention, Decoder, Seq2Seq
from data import BertDataset
from run import train, eval
from run.utils.time import epoch_time

def extract_name(input_list):
    name = ''
    i = 0
    try:
        while (input_list[i] != '<'):
            i += 1
            pass
        i += 1
        while (input_list[i] != '>'):
            name += input_list[i] + ' '
            i += 1
        return name[:-1].replace(" ##", "")

    except Exception as e:
        print("Error extracting name on", input_list)
        return "name"


_suffix1, _suffix2, _suffix3 = "_suffix1", "_suffix2", "_suffix3"


def get_suffix(word: str, sffx_type: str):
    suffix = ''
    if sffx_type == "_suffix1":
        suffix = Turkish(word).genitive(proper_noun=True) # -in
    elif sffx_type == "_suffix2":
        suffix = Turkish(word).dative(proper_noun=True)  # -e
    elif sffx_type == "_suffix3":
        suffix = Turkish(word).ablative(proper_noun=True) #-den
    elif sffx_type == "_suffix4":
        suffix = Turkish(word).ablative(proper_noun=True)
    suffix = str(suffix)
    return suffix[len(word):] 


def format_question(name, question_pattern):
    try:
        if _suffix1 in question_pattern:
            question_pattern = question_pattern.format(
                    name=name, _suffix1=get_suffix(name, _suffix1))
        elif _suffix2 in question_pattern:
            question_pattern = question_pattern.format(
                    name=name, _suffix2=get_suffix(name, _suffix2))
        elif _suffix3 in question_pattern:
            question_pattern = question_pattern.format(
                    name=name, _suffix3=get_suffix(name, _suffix3))
        else:
            question_pattern = question_pattern.format(name=name)
        return question_pattern
    except Exception as e:
        print("Error on: {} - {} \n{}\n".format(e, name, question_pattern))
        return question_pattern


def format_sentence_list(raw_content, names):
    formatted_questions = []
    for i, line in enumerate(raw_content):
        line = line[1:3]
        formatted_lines = []
        special_case = False
        for question in line:
            formatted_line = ''
            for token in question:
                if token == "[SEP]":
                    continue
                elif token[0] == "#" or token == "." or special_case:
                    formatted_line += token.replace('#', '').replace("'",'')
                    special_case = False
                elif token == "{" or token == "_":
                    formatted_line += token
                    special_case = True
                elif token == "}":
                    formatted_line += token
                elif token == "?":
                     formatted_line += "?" 
                     break
                else:
                    formatted_line += " " + token.replace('#', '').replace("'",'')
                    special_case = False
            formatted_lines.append(format_question(names[i], formatted_line.replace("_ s", "_s")))
            print(formatted_lines)
        formatted_questions.append(formatted_lines)
    return formatted_questions


def bleu_score(prediction, ground_truth):
    prediction = prediction.max(2)[1]
    bleu_list = []

    for x, y in zip(ground_truth, prediction):
        x = tokenizer.convert_ids_to_tokens(x.tolist())
        y = tokenizer.convert_ids_to_tokens(y.tolist())
        idx1 = x.index('[SEP]') if '[SEP]' in x else len(x)
        idx2 = y.index('[SEP]') if '[SEP]' in y else len(y)

        bleu_list.append((bleu([x[1:idx1]], y[1:idx2], [0.25, 0.25, 0.25, 0.25],
            smoothing_function=SmoothingFunction().method4), x[1:idx1], y[1:idx2]))
        return (max(bleu_list, key=lambda x: x[0]))

def loss(prediction, ground_truth):
    criterion = nn.CrossEntropyLoss(ignore_index=0, reduction='none')
    train_loss = []
    for x, y in zip(ground_truth, prediction):
        w = tokenizer.convert_ids_to_tokens(x.tolist())
        z = tokenizer.convert_ids_to_tokens(y.max(1)[1].tolist())
        idx1 = w.index('[SEP]') if '[SEP]' in w else len(w)
        idx2 = z.index('[SEP]') if '[SEP]' in z else len(z)
        loss = criterion(y, x.to(device))
        loss = loss.sum()
        train_loss.append((loss, w[1:idx1], z[1:idx2]))
    return (max(train_loss, key=lambda x: x[0]))


tokenizer = BertTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
def generate_sentences(filename, is_request=True):
    enable_reproducibility(121314)
    dataset_path = filename if not is_request else f"requests/{filename}"
    valid_set = BertDataset(bert_path / bert_model / dataset_path)
    valid_loader = DataLoader(valid_set, batch_size=1, shuffle=True, num_workers=dl_workers, pin_memory=True if device == 'cuda' else False)

    attention = Attention(bert_hidden_size, decoder_hidden_size)
    decoder = Decoder(bert_vocab_size, decoder_input_size, bert_hidden_size, decoder_hidden_size, dropout, attention, device)
    model = Seq2Seq(decoder, device)
    print("../data/model/bert-base-cased")

    encoder = BertModel.from_pretrained("../data/model/dbmdz/bert-base-turkish-cased/" + "model0epoch" + str(epochs - 1))
    encoder.to(device)
    f = open("../data/model/decoder/model0epoch" + str(epochs - 1), 'rb')
    _, model_dict, _, _, _, _ = load_checkpoint(f)
    model.load_state_dict(model_dict)

    model.to(device)
    bleu_list = []
    loss_list = []
    names_list = []
    with torch.no_grad():
        for i, (input_, output_) in enumerate(valid_loader):
            input_data, input_length = input_
            output_data, output_length = output_
            names_list.append(extract_name(tokenizer.convert_ids_to_tokens(input_data[0][0])))
            input_ids, token_type_ids, attention_mask = input_data
            
            bert_hs = encoder(input_ids.to(device), token_type_ids=token_type_ids.to(device),
            		attention_mask=attention_mask.to(device))
            
            prediction = model(bert_hs[0], output_data.to(device), 0)
            loss_list.append(loss(prediction, output_data.to(device)))
        f_list = format_sentence_list(loss_list[0:], names_list)
        return f_list

if __name__ == '__main__':
    generate_sentences('test', False)
