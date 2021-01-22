import torch

class Bert_SQG(torch.nn.Module):
    def __init__(self, model, tokenizer):
        super(Bert_SQG, self).__init__()
        self.model = model
        self.tokenizer = tokenizer
        self.linear = torch.nn.Linear(768, tokenizer.vocab_size)

    def forward(self, x):
        tokens = torch.tensor([self.tokenizer.encode(x, add_special_tokens=False, max_length=510)])

        last_hidden_states = model(tokens)[0]
        mask_token_h_state = last_hidden_states[:, -1, :]
    
        linear_output = self.linear(mask_token_h_state)    
        return linear_output