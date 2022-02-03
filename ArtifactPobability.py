


class ArtifactProbability:
    

    def __init__ (self):

        self.circlet = {

            "ATK%main" : 0.22,
            "HP%main" : 0.22,
            "DEF%main" : 0.22,
            "CR%main" : 0.10,
            "CD%main" : 0.10,
            "HB%main" : 0.10,
            "EMmain" : 0.04,

            "ATK%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "HP%" : 0.1,
                "DEF%" : 0.1,
                "ER%" : 0.1,
                "EM" : 0.1,
                "CR" : 0.075,
                "CD" : 0.075
            },

            "HP%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.1,
                "DEF%" : 0.1,
                "ER" : 0.1,
                "EM" : 0.1,
                "CR" : 0.075,
                "CD" : 0.075
            }, 

            "DEF%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.1,
                "HP%" : 0.1,
                "ER%" : 0.1,
                "EM" : 0.1,
                "CR" : 0.075,
                "CD" : 0.075
            },
            
            "CR%" : {
                "HP" : 0.1463,
                "ATK" : 0.1463,
                "DEF" : 0.1463,
                "ATK%" : 0.976,
                "HP%" : 0.976,
                "ER%" : 0.976,
                "EM" : 0.976,
                "CD" : 0.0732
            },

            "CD%" : {
                "HP" : 0.1463,
                "ATK" : 0.1463,
                "DEF" : 0.1463,
                "ATK%" : 0.976,
                "HP%" : 0.976,
                "ER%" : 0.976,
                "EM" : 0.976,
                "CR" : 0.0732
            },

            "HB%" : {
                "HP" : 0.1364,
                "ATK" : 0.1364,
                "DEF" : 0.1364,
                "ATK%" : 0.0909,
                "HP%" : 0.0909,
                "ER%" : 0.0909,
                "EM" : 0.0682,
                "CR" : 0.0682
            },

            "EM" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.0909,
                "HP%" : 0.0909,
                "ER%" : 0.0909,
                "CD" : 0.075,
                "CR" : 0.075
            }


        }

        self.goblet = {

            "ATK%main" : 0.2125,
            "HP%main" : 0.2125,
            "DEF%main" : 0.2,
            "HB%main" : 0.10,
            "PyroB%main" : 0.05,
            "ElectroB%main" : 0.05,
            "CryoB%main" : 0.05,
            "HydroB%main" : 0.05,
            "AnemoB%main" : 0.05,
            "GeoB%main" : 0.05,
            "PhysB%main" : 0.05,
            "EM%main" : 0.025,

            "ATK%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "HP%" : 0.1,
                "DEF%" : 0.1,
                "ER%" : 0.1,
                "EM" : 0.1,
                "CR" : 0.075,
                "CD" : 0.075
            },

            "HP%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.1,
                "DEF%" : 0.1,
                "ER" : 0.1,
                "EM" : 0.1,
                "CR" : 0.075,
                "CD" : 0.075
            }, 

            "DEF%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.1,
                "HP%" : 0.1,
                "ER%" : 0.1,
                "EM" : 0.1,
                "CR" : 0.075,
                "CD" : 0.075
            },
            
            "EB%" : {
                "HP" : 0.1364,
                "ATK" : 0.1364,
                "DEF" : 0.1364,
                "DEF%" : 0.0909,
                "ATK%" : 0.0909,
                "HP%" : 0.0909,
                "ER%" : 0.0909,
                "EM" : 0.0909,
                "CR" : 0.0682,
                "CD" : 0.0682
            },

            "EM" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.1,
                "HP%" : 0.1,
                "ER%" : 0.1,
                "DEF%" : 0.1,
                "CD" : 0.075,
                "CR" : 0.075
            }


        }

        self.sands = {

            "ATK%main" : 0.2668,
            "HP%main" : 0.2668,
            "DEF%main" : 0.2668,
            "ER%main" : 0.10,
            "EMmain" : 0.10,

            "ATK%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "HP%" : 0.1,
                "DEF%" : 0.1,
                "ER%" : 0.1,
                "EM" : 0.1,
                "CR" : 0.075,
                "CD" : 0.075
            },

            "HP%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.1,
                "DEF%" : 0.1,
                "ER" : 0.1,
                "EM" : 0.1,
                "CR" : 0.075,
                "CD" : 0.075
            }, 

            "DEF%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.1,
                "HP%" : 0.1,
                "ER%" : 0.1,
                "EM" : 0.1,
                "CR" : 0.075,
                "CD" : 0.075
            },
            
            "ER%" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.1,
                "HP%" : 0.1,
                "DEF%" : 0.1,
                "EM" : 0.1,
                "CD" : 0.075,
                "CR" : 0.075
            },

            "EM" : {
                "HP" : 0.15,
                "ATK" : 0.15,
                "DEF" : 0.15,
                "ATK%" : 0.10,
                "HP%" : 0.10,
                "DEF%" : 0.10,
                "ER%" : 0.10,
                "CD" : 0.075,
                "CR" : 0.075
            }

        }


    def getMainStatProb(self, artifactSlot, mainStat):

        return self.selectArtifactSlot(artifactSlot)[mainStat]
    
    

    def selectArtifactSlot(self, artifactSlot):

        Stats = {
                "circlet" : self.circlet,
                "goblet" : self.goblet,
                "sands" : self.sands
            }

        return Stats[artifactSlot]

    def getSubStatProb(self, artifactSlot, mainStatTag, subStat):

        return self.selectArtifactSlot(artifactSlot)[mainStatTag][subStat]


test = ArtifactProbability()

keys = list()

pyroBonusProb = test.getMainStatProb("goblet", "PyroB%main")
subProb1 = test.getSubStatProb("goblet", "EB%", "ATK%")
subProb2 = test.getSubStatProb("goblet", "EB%", "CR")
subProb3 = test.getSubStatProb("goblet", "EB%", "CD")

print(pyroBonusProb)
print(subProb1)
print(subProb2)
print(subProb3)

totalProb = pyroBonusProb*subProb1*subProb2*subProb3
number_of_artifacts = int( 1 / totalProb)

print(totalProb)
print(number_of_artifacts)