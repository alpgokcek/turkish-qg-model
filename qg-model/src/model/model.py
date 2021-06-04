import random

import torch
from torch import nn
import torch.nn.functional as F


class Attention(nn.Module):
    """Implements additive attention and return the attention vector used to weight the values.
        Additive attention consists in concatenating key and query and then passing them trough a linear layer."""

    def __init__(self, enc_hid_dim, dec_hid_dim):
        super().__init__()

        self.enc_hid_dim = enc_hid_dim
        self.dec_hid_dim = dec_hid_dim

        self.attn = nn.Linear(enc_hid_dim + dec_hid_dim, dec_hid_dim)
        self.v = nn.Parameter(torch.rand(dec_hid_dim))

    def forward(self, key, queries):
        batch_size = queries.shape[0]
        src_len = queries.shape[1]
        key = key.unsqueeze(1).repeat(1, src_len, 1)
        energy = torch.tanh(self.attn(torch.cat((key, queries), dim=2)))
        energy = energy.permute(0, 2, 1)
        v = self.v.repeat(batch_size, 1).unsqueeze(1)
        attention = torch.bmm(v, energy).squeeze(1)
        return F.softmax(attention, dim=1)


class Decoder(nn.Module):
    def __init__(self, output_dim, emb_dim, enc_hid_dim, dec_hid_dim, dropout, attention, device):
        super().__init__()

        self.device = device

        self.emb_dim = emb_dim
        self.enc_hid_dim = enc_hid_dim
        self.dec_hid_dim = dec_hid_dim
        self.output_dim = output_dim
        self.dropout = dropout
        self.attention = attention

        self.embedding = nn.Embedding(output_dim, emb_dim)
        self.rnn = nn.GRU(enc_hid_dim + emb_dim, dec_hid_dim, batch_first=True, num_layers=1)
        self.out = nn.Linear(enc_hid_dim + dec_hid_dim + emb_dim, output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, input, queries, key):
        input = input.unsqueeze(1)
        embedded = self.dropout(self.embedding(input))
        a = self.attention(key, queries)
        a = a.unsqueeze(1)

        weighted = torch.bmm(a, queries)
        rnn_input = torch.cat((embedded, weighted), dim=2)
        output, hidden = self.rnn(rnn_input, key.unsqueeze(0))

        embedded = embedded.squeeze(1)
        output = output.squeeze(1)
        weighted = weighted.squeeze(1)

        output = self.out(torch.cat((output, weighted, embedded), dim=1))
        return output, hidden.squeeze(0)

class Seq2Seq(nn.Module):
    def __init__(self, decoder, device):
        super().__init__()

        self.decoder = decoder
        self.device = device

    def forward(self, src, trg, teacher_forcing_ratio=0.5):
        batch_size = src.shape[0]
        max_len = trg.shape[1]
        trg_vocab_size = self.decoder.output_dim
        outputs = torch.zeros(batch_size, max_len, trg_vocab_size).to(self.device)
        output = trg[:, 0]

        hidden = torch.zeros(output.shape[0], self.decoder.dec_hid_dim).to(self.device)

        for t in range(1, max_len):
            output, hidden = self.decoder(output, src, hidden)
            outputs[:, t] = output
            teacher_force = random.random() < teacher_forcing_ratio
            top1 = output.max(1)[1]
            output = (trg[:, t] if teacher_force else top1)

        return outputs


import torch.nn.functional as F
from torch import nn
import torch


class BeamSearch(nn.Module):

    def __init__(self, decoder, device, k):
        super().__init__()
        self.decoder = decoder
        self.device = device
        self.k = k

    def forward(self, src):
        batch_size = src.shape[0]
        max_len = 40
        trg_vocab_size = self.decoder.output_dim

        search_results = torch.zeros(batch_size, self.k, max_len).type(torch.LongTensor).to(self.device)
        search_map = torch.zeros(batch_size, self.k, max_len).type(torch.LongTensor).to(self.device)
        outputs = torch.zeros(batch_size, max_len).type(torch.LongTensor).to(self.device)
        hiddens = torch.zeros(batch_size, self.k, self.decoder.dec_hid_dim).to(self.device)
        ended = torch.zeros(batch_size, self.k).to(self.device)
        true = torch.ones(ended.shape).to(self.device)
        no_prob = torch.Tensor(batch_size, trg_vocab_size).fill_(float('-Inf')).to(self.device)
        no_prob[:, 102] = 0
        lengths = torch.zeros(batch_size, self.k).to(self.device)

        output = torch.Tensor(batch_size).fill_(102).type(torch.LongTensor).to(self.device)
        hidden = torch.zeros(output.shape[0], self.decoder.dec_hid_dim).to(self.device)

        output, hidden = self.decoder(output, src, hidden)
        output = F.log_softmax(output, dim=1)

        for i in range(self.k):
            hiddens[:, i, :] = hidden

        scores, search_results[:, :, 0] = torch.topk(output, self.k, 1)

        for t in range(1, max_len):
            candidates = torch.Tensor(batch_size, 0).to(self.device)
            for i in range(self.k):

                idx = search_map[:, 0, t - 1].unsqueeze(1).unsqueeze(1)
                idx = idx.expand(-1, -1, hiddens.shape[2])
                hidden = hiddens.gather(1, idx).squeeze(1).squeeze(1)

                output, hiddens[:, i, :] = self.decoder(search_results[:, i, t - 1], src,
                                                        hidden)
                output = F.log_softmax(output, dim=1)

                output = torch.where(ended[:, i].unsqueeze(1).expand_as(output) == 0, output, no_prob)
                lengths[:, i] = torch.where(ended[:, i] == 0, lengths[:, i] + 1, lengths[:, i])

                output = output + scores[:, i].unsqueeze(1)

                candidates = torch.cat((candidates, output), 1)

            norm_cand = torch.tensor(candidates)

            for i in range(self.k - 1):
                norm_cand[:, trg_vocab_size * i:trg_vocab_size * (i + 1)] /= (lengths[:, i] ** 0.7).unsqueeze(1)

            _, topk = torch.topk(norm_cand, self.k, 1)

            for i in range(topk.shape[0]):
                scores[i, :] = candidates[i, topk[i, :]]

            ended = torch.where((topk - (topk / trg_vocab_size) * trg_vocab_size) == 102, true, ended)
            search_results[:, :, t] = topk - (
                    topk / trg_vocab_size) * trg_vocab_size
            search_map[:, :, t] = topk / trg_vocab_size

        _, idx = torch.max(scores, 1)

        for t in range(max_len - 1, -1, -1):
            outputs[:, t] = search_results[:, :, t].gather(1, idx.unsqueeze(1)).squeeze(1)
            idx = search_map[:, :, t].gather(1, idx.unsqueeze(1)).squeeze(1)
        return outputs