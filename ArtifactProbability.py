


from sqlalchemy import null
import math


class ArtifactProbability:
    


    circlet = {

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

    goblet = {

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

    sands = {

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

    def __init__ (self):
        pass

    def get_main_stat_prob(self, artifactType, mainStat):

        returnValue = null

        if artifactType == "circlet":
            returnValue = self.circlet

        elif artifactType == "goblet":
            returnValue = self.goblet

        elif artifactType == "sands":
            returnValue = self.sands
        
        return returnValue, artifactType

    # function for calculating the substat probability of an artifact specifying certain substats
    def calc_substat_probabilty(main_stat_prob, mainstat, *substats):

        mainstat_key = main_stat_prob + "main"
        mainstat_probability = main_stat_prob[mainstat_key]
        
        substat_probabilities = []
        total_probability = 1

        # looping through every substat and adding it to a list / getting the total probabilty
        for substat in substats:

            # extracting the probaiblity values from the nested hard coded dictionaries
            substat_probability = main_stat_prob[mainstat][substat]
            substat_probabilities.append(substat_probability)

            # sum of all the current probabilities
            new_term = substat_probability / (1 - sum(substat_probabilities))

            # multiplying the previous terms by the new term
            total_probability = total_probability * new_term

        return total_probability

        # next we will want to find the probability of rolling n times into a certain number of substats
        # we can probably do that by just calculating a binomial distribution for whatever stat we are interested in
        # pass the function a series of values for which slot we want to roll into and how many times

        # once an artifact gets 4 substats it starts to use this function
    def substat_probability(substat_list, substat_probabilities, roll_list):

        # to calculate the probability of getting a specific number of rolls we will add the binomial distributions
        # of rolling each of the substats n times

        probability = 1

        for roll in roll_list:

            # calculate probability of getting n rolls in k attempts
                
            new_stat = math.comb(roll, roll)*(0.25**roll)*(1-0.25)**(roll-roll)

            probability = probability*new_stat












    # we need to first get the probability of rolling a certain artifact and then get the subsequent rolls.

    # we could also try to define all of the artifacts but lets leave that for later.


        

    
