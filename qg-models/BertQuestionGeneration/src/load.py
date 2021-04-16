import torch
import transformers 


checkpoint = torch.load("../data/model/stage_one/dbmdz/bert-base-turkish-cased/model0epoch2/pytorch_model.bin", map_location=None)
#checkpoint = torch.load("../data/model/stage_one/bert-base-cased/model0epoch3/pytorch_model.bin", map_location=None)

print(checkpoint.keys())
