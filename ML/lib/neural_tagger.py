from ML.tagger import Tagger
import matplotlib.pyplot as plt
from config import *
import numpy as np
import torch

class NeuralTagger(Tagger):

    def __init__(self, network):
        self.model = network

    def predict(self, state, targets):
        inp = torch.tensor(state.get(), dtype=torch.float)
        scores = self.model.forward(inp)
        #TODO: pick the best and valid 
        if HEAT_MAP:
            result = []
            #create a matix with 9 coloms 
            data = list(map(float, scores))
            for i in range(len(data)//10):
                begin = i*10
                end = (i+1)*10
                result.append(data[begin : end])
            fig = plt.figure(figsize=(state.higth, state.width))
            fig.add_subplot(1, 2, 1)
            plt.imshow(np.array(result), cmap='hot', interpolation='nearest')
            fig.add_subplot(1, 2, 2)
            plt.imshow(np.array(state.get_map()) * 10, cmap='bwr', interpolation=None)
            plt.savefig("heatmap/out")
            plt.close(fig)
        res = []
        for c,s in enumerate(scores):
            res.append((c,s))
        for c,s in sorted(res, key=lambda x:x[1], reverse=True):
            x,y = targets[c]
            if state.free(x,y):
                return x,y

        raise("No moves left")