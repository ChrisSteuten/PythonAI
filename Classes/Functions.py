from math import e

def WeightedSum(inputConnectionsList = []):
        tempFloat = 0.0
        for element in inputConnectionsList:
            tempFloat = tempFloat + (element.GetValue() * element.GetWeight())
        return tempFloat

def RELU(inputFloat = 0):
        if inputFloat < 0:
            return 0

        return inputFloat

def Sigmoid(inputFloat = 0):
        return (1 / (1 + e - inputFloat))

activationFunctions = [
    RELU(),
    Sigmoid()
]

