from ML.neural_tagger_trainer import train_neural
from ML.nn_agent import NN_Agent
from ML.training_agent import Train
from ML.evaluvate import bench
from lib.world import World
from lib.state import State
from lib.ship import Ship
from config import *
from time import time
from random import shuffle
import torch
      
def main(model, save=None):
    print(model)
    if model == "init":
        model = ""
    else:
        model = f"ML/models/{model}"
    start = time()
    print("Started Taining")
    network , optimizer = train_neural(Train ,State , World, Ship, n=TRAINING_ROUNDS, model=model)
    print("Training Done in {:.2f} s".format((time() - start)))
    #TODO: save to file
    print(bench(network, BENCHMARK))
    if save == None:
        imp = input("Name of the model:")
        if imp != "":
            model = imp
    else:
        model = save
    torch.save({
            'model_state_dict': network.model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            }, f"ML/models/{model}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        main("")
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])