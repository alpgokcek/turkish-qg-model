from transformers import AutoModelForTokenClassification, BertTokenizer, pipeline, BertModel
import pickle, json, re, torch
from tqdm import notebook
from torch.utils.data import Dataset, DataLoader
from Dataset_loader import Dataset_loader
from Bert_SQG import Bert_SQG

epoch_count = 10
base_path, device = "data", "cuda"

# static paths
berturk_path, pretrained_path, dataset_path = "{}/bert-base-turkish-cased".format(base_path), "{}/pretrained".format(base_path), '{}/optimized_out_data.txt'.format(base_path)

# load the language model
tokenizer, model = BertTokenizer.from_pretrained(berturk_path), BertModel.from_pretrained(berturk_path)

model.save_pretrained(pretrained_path) 
tokenizer.save_pretrained(pretrained_path)

torch.set_default_tensor_type(torch.cuda.FloatTensor)

# load the data
dataloader = Dataset_loader(dataset_path)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

# init model
bert_sqg = Bert_SQG(model, tokenizer)
bert_sqg.to(device)

# cleaning the dataset data
def clean_data(item):
  context = ' '.join([re.sub(r'[\W_]', '', w.lower()) for w in item['description'].split(' ')])
  question = ' '.join([re.sub(r'[\W_]', '', w.lower()) for w in item['data'][0]['questions'][0].split(' ')])
  answer = ' '.join([re.sub(r'[\W_]', '', w.lower()) for w in item['data'][0]['answer'].split(' ')])
  return context, question, answer

for epoch in range(epoch_count):
  bert_sqg.train()
  for item in notebook.tqdm_notebook(dataloader):
      context, question, answer = clean_data(item)
      output_question = ''
      
      # create the input sequence
      x = tokenizer.cls_token + ' ' + context + ' ' + tokenizer.sep_token + ' ' + answer + ' ' + tokenizer.sep_token + ' ' + tokenizer.mask_token 
      
      for word in question.split(' '):
          target = torch.tensor(tokenizer.encode(word, add_special_tokens=False))[:1]
          out = bert_sqg(x)
          try:
            loss = criterion(out, target)
          except ValueError:
            continue
          loss.backward()
          torch.nn.utils.clip_grad_norm_(model.parameters(), 0.5)
          optimizer.step()
        
          predicted_word = tokenizer.convert_ids_to_tokens([torch.argmax(torch.nn.Softmax(dim = 1)(out))])
          output_question += ' {}'.format(predicted_word[0])
          x = tokenizer.cls_token + ' ' + context + ' ' + tokenizer.sep_token + ' ' + answer + ' ' + tokenizer.sep_token + ' ' + output_question + ' ' + tokenizer.mask_token 

      print(output_question)
    
  torch.save(bert_sqg.state_dict(), '{}/BERT_SQG_{}_epochs.pt'.format(base_path, str(epoch+1)))