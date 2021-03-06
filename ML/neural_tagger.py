from ML.tagger import Tagger
from ML.network import Network
import matplotlib.pyplot as plt
from config import *
import numpy as np
import torch
import random

class NeuralTagger(Tagger):

    def __init__(self):
        self.model = Network()

    def predict(self, state, targets):
        if torch.cuda.is_available() and GPU:
            inp = state.get2d().cuda()
        else:
            inp = state.get2d()
        scores = self.model.forward(inp[None,])
        #scores = torch.nn.functional.softmax(scores, dim=1)
        #TODO: pick the best and valid 
        if HEAT_MAP:
            print(scores)
            fig = plt.figure(figsize=(state.higth, state.width))
            fig.add_subplot(1, 2, 1)
            plt.imshow(scores[0,1].cpu().detach().numpy(), cmap='hot', interpolation='nearest')
            fig.add_subplot(1, 2, 2)
            plt.imshow(np.array(state.get_map()) * 10, cmap='bwr', interpolation=None)
            plt.savefig("heatmap/out")
            plt.close(fig)
        res = []
        for c,s in enumerate(scores[0,1].reshape(-1)):
            res.append((c,s))
        random.shuffle(res)
        for c,s in sorted(res, key=lambda x:x[1], reverse=True):
            x,y = targets[c]
            if state.free(x,y):
                return x,y

        raise("No moves left")