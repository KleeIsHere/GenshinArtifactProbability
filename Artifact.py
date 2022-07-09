from re import S
from sqlalchemy import null
import ArtifactProbability
import itertools

class Artifact:

    probabilities = ArtifactProbability.ArtifactProbability()
    numSubstats = null
    mainStat = null
    substats = []
    substatProbabilities = []

    def __init__(self):
        pass

    def initializeUserStats(self, artifactType, main, substats) :

        self.mainStat = main

        self.numSubstats = len(substats)
        
        for substat in substats:

            self.substats.append(substat)

            self.substatProbabilities.append(self.probabilities.getMainStatProb(artifactType, main))


            print(self.substats)



    def getArtifactOccuranceProbability(self):

        

        # split the list of substats into dictionary keys
        
            


        cr = .0789
        cd = .0789
        em = .1053
        hp = .1053

        occurance = 0.0

        for a, b, c, d in itertools.permutations((cr, cd, em, hp), 4):
            step = a * (b/(1-a)) * (c/(1-a-b)) * (d/(1-a-b-c))
            occurance += step
            print("step: " + str(step))

        print("probability to get this artifact: " + str(occurance))
        print("number of artifacts to get:" + str(1/occurance))





        

        pass



        


test = Artifact()

userMainStat = "CD%main"
userSubstats = ["HP", "ATK", "CD"]

test.initializeUserStats(userMainStat, userSubstats)
print(test.getArtifactProbability())
        




