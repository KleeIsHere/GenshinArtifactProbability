from random import seed
import Artifact
import math
import numpy as np

class ArtifactGenerator:

    def __init__(self):
        pass

    def generateArtifact(self, substats):

        # get a random number between 0 and 1000000

        randGenerator = np.random.default_rng(None)

        possibleMainStats = ["ATK%main", "HP%main", "DEF%main", "ER%main", "EMmain"]

        possibleSubstats = ["HP", "ATK","DEF","HP%","DEF%","ER%","EM","CR","CD"]

        A

        



        randMainStat = randGenerator.random()

        return rand


        # split the dataset into portions based on the probability 


test = ArtifactGenerator()


mainStat = "ATK%main"
substats = ['ATK%', ]

print(test.generateArtifact(4))
