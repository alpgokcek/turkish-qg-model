import logging
logging.basicConfig(filename="example.log",  level=logging.DEBUG)
logging.getLogger('transformers').setLevel(logging.WARNING)
log = logging.getLogger(__name__)

import time
import math
import os

import torch
from torch import optim, nn, cuda
from transformers import AdamW
from torch.utils.data import DataLoader
from transformers import BertModel

from config import checkpoint, bert_path, mb, dl_workers, device, bert_hidden_size, decoder_hidden_size, \
    bert_vocab_size, decoder_input_size, dropout, epochs, clip, model_path, bert_model, encoder_trained, \
    attention_hidden_size, num_layers, weight_decay, betas, lr, momentum
from model.utils import load_checkpoint, init_weights, save_checkpoint, enable_reproducibility, model_size, no_grad
from model import Attention, Decoder, Seq2Seq, BeamSearch
from data import BertDataset
from run import train, eval
from run.utils.time import epoch_time

if __name__ == '__main__':
    log = logging.getLogger(__name__)
    log.info(f'Running on device {cuda.current_device() if device=="cuda" else "cpu"}')

    enable_reproducibility(121314)

    train_set = BertDataset(bert_path / bert_model / 'train')
    valid_set = BertDataset(bert_path / bert_model / 'valid')
    training_loader = DataLoader(train_set, batch_size=mb, shuffle=True,
                                 num_workers=dl_workers, pin_memory=True if device == 'cuda' else False)
    valid_loader = DataLoader(valid_set, batch_size=mb, shuffle=True,
                              num_workers=dl_workers, pin_memory=True if device == 'cuda' else False)

    print(len(training_loader))
    attention = Attention(bert_hidden_size, decoder_hidden_size)
    decoder = Decoder(bert_vocab_size, decoder_input_size, bert_hidden_size, decoder_hidden_size, dropout, attention, device)
    model = Seq2Seq(decoder, device)

    encoder = BertModel.from_pretrained(model_path / bert_model)
    encoder.to(device)

    optimizer = optim.Adam(decoder.parameters())
    criterion = nn.CrossEntropyLoss(ignore_index=0, reduction='none')
    if checkpoint is not None:
        last_epoch, model_dict, optim_dict, valid_loss_list, train_loss_list, bleu_list = load_checkpoint(checkpoint)
        last_epoch += 1
        model.load_state_dict(model_dict)
        best_valid_loss = min(valid_loss_list)

        optimizer.load_state_dict(optim_dict)
        for state in optimizer.state.values():
            for k, v in state.items():
                if torch.is_tensor(v):
                    state[k] = v.to(device)

        log.info(f'Using checkpoint {checkpoint}')
    else:
        last_epoch = 0
        valid_loss_list, train_loss_list = [], []
        model.apply(init_weights)

    model.to(device)


    for epoch in range(last_epoch, epochs):
        start_time = time.time()
        print("epoch:", epoch)
        log.info(f'Epoch {epoch+1} training')
        train_loss = train(model, device, training_loader, optimizer, criterion, clip, encoder, encoder_trained)
        log.info(f'\nEpoch {epoch + 1} validation')
        valid_loss, bleu_score = eval(model, device, valid_loader, criterion, encoder)

        train_loss_list.append(train_loss)
        valid_loss_list.append(valid_loss)

        end_time = time.time()
        print("time took:",end_time-start_time)
        epoch_mins, epoch_secs = epoch_time(start_time, end_time)
        
        save_checkpoint(model_path /f'decoder/model0epoch{epoch}', epoch, model, optimizer, valid_loss_list, train_loss_list, bleu_score)
        tmp_path ="{}/{}/{}/model0epoch{}".format(model_path,bert_model,epoch)
        os.mkdir(tmp_path)
        encoder.save_pretrained(tmp_path)
        log.info(f'\nEpoch: {epoch + 1:02} completed | Time: {epoch_mins}m {epoch_secs}s')
        log.info(f'\tTrain Loss: {train_loss:.3f} | Train PPL: {math.exp(train_loss):7.3f}')
        log.info(f'\t Val. Loss: {valid_loss:.3f} |  Val. PPL: {math.exp(valid_loss):7.3f} | Val. BLEU {bleu_score}\n\n')
