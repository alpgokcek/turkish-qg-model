import torch
import transformers 


checkpoint = torch.load("../data/model/stage_one/bert-base-cased/model0epoch3/pytorch_model.bin", map_location=None)

print(checkpoint.keys())
