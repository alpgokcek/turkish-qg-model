import torch
import transformers 

checkpoint = torch.load("../data/model/dbmdz/bert-base-turkish-cased/model0epoch2/pytorch_model.bin", map_location=None)
print(checkpoint.keys())
