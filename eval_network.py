from ML.evaluvate import bench
from ML.neural_tagger_trainer import load_model
from config import *

if __name__ == "__main__":
    #main()
    models = [f"ML/models/10H1700k"]
    print("Benshmarking with", BENCHMARK, "games")
    for model in models:
        agent = load_model(model)
        print("{:.2f} moves: {}".format(bench(agent, BENCHMARK), model))