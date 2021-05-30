import json
import pickle
from pprint import pprint
import numpy as np
import torch
from pytorch_transformers import BertTokenizer
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer

class Preprocess:

    def __init__(self, squad_path, bert_model):
        with open(squad_path, 'r') as read_file:
            data = json.load(read_file)
        input, output = _extract_squad_data(data)
        self.data = _tokenize_data(input, output, bert_model)


    def save(self, path):
        with open(path, 'wb') as write_file:
            pickle.dump(self.data, write_file)


def _extract_squad_data(data):
    data = data['data']

    input = []
    output = []
    print(len(data))
    for doc in data:
        context = doc['description'][:512]
        for qas in doc['data']:
            answer = qas['answer']
            question = qas['questions'][0]
            input.append((context, answer))
            output.append(question)
    input = input[:int(0.1 * len(input))]  
    output = output[:int(0.1 * len(output))]
    return input, output


def _tokenize_data(input, output, bert_model):
    tokenizer = BertTokenizer.from_pretrained(bert_model)

    data = tokenizer.batch_encode_plus(input, pad_to_max_length=False, padding=True, return_tensors='pt')
    out_dict = tokenizer.batch_encode_plus(output, pad_to_max_length=False, padding=True,  return_tensors='pt')

    data['output_ids'] = out_dict['input_ids']
    data['output_len'] = out_dict['attention_mask'].sum(dim=1)
    data['input_len'] = data['attention_mask'].sum(dim=1)

    idx = (data['input_len'] <= 512)
    in_m = max(data['input_len'][idx])
    out_m = max(data['output_len'][idx])

    data['input_ids'] = data['input_ids'][idx, :in_m]
    data['attention_mask'] = data['attention_mask'][idx, :in_m]
    data['token_type_ids'] = data['token_type_ids'][idx, :in_m]
    data['input_len'] = data['input_len'][idx]

    data['output_ids'] = data['output_ids'][idx, :out_m]
    data['output_len'] = data['output_len'][idx]

    return data

dataset = Preprocess('data.json', 'dbmdz/bert-base-turkish-cased')
dataset.save(f'data')
