import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

import json
from pathlib import Path
import torch

from transformers import BertModel

from data import Preprocess


def setup(bert_model, model_path, turquad_path, bert_path):
    log = logging.getLogger(__name__)

    file = Path('.setup').open('a+')
    file.seek(0, 0)

    if bert_model in (file.readline().split()):
        file.close()
        log.info(f'Setup: {bert_model} setup already performed')
        return
    file.write(f' {bert_model} ')
    file.close()

    log.info(f'Setup: downloading {bert_model}')
    BertModel.from_pretrained(bert_model).save_pretrained(model_path / bert_model)

    log.info(f'Setup: preprocessing {bert_model} input')
    for x in turquad_path.iterdir():
        if x.is_file():
            dataset = Preprocess(turquad_path / x.name, bert_model)
            dataset.save(bert_path / bert_model / x.name[11:-5])
    log.info(f'Setup: {bert_model} setup completed')


# runtime environment
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# paths
turquad_path = Path('../data/turquad')
bert_path = Path('../data/bert')
model_path = Path('../data/model/')

bert_model = 'dbmdz/bert-base-turkish-cased'

# if not present download the right bert version and preprocess and save the dataset
setup(bert_model, model_path, turquad_path, bert_path)

# encoder parameter

with (model_path / bert_model / 'config.json').open('r') as f:
    conf = json.load(f)
    bert_hidden_size = conf['hidden_size']
    bert_vocab_size = conf['vocab_size']

#optimizer
weight_decay = 0.001
betas = (0.9, 0.999) # only for Adam
lr = 0.00005
momentum = 0.9 # only for SGD

# decoder parameter
decoder_hidden_size = 512
decoder_input_size = 512  # embedding dimesions
attention_hidden_size = 512
num_layers = 1
clip = 1
dropout = 0.1

# training parameters
epochs = 3
mb = 28
dl_workers = 0
checkpoint = None
encoder_trained = False
