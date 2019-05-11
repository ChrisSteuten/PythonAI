import threading
from .BrainArea import BrainArea

class Brain(object):
    __name = ''
    __brainAreas = []

    def __init__(self,parName):
        self.__name = parName

    def __str__(self):
        tempString = ''
        for brainArea in self.__brainAreas:
            tempString += '/' + str(brainArea)
        return tempString

    def GetBrainAreas(self):
        return self.__brainAreas

    def GetBrainArea(self, key):
        return self.__brainAreas[key]

    def GetBrainAreasCount(self):
        return len(self.__brainAreas)

    def AddBrainArea(self, parBrainArea=None):
        if not parBrainArea: parBrainArea = BrainArea()
        self.__brainAreas.append(parBrainArea)

    def GetAllNeurons(self):
        tempNeuronList = []
        for brainArea in self.__brainAreas:
            tempNeuronList.extend(brainArea.GetAllNeurons())
        return tempNeuronList

    def ActivateBrainArea(self, parNo, inputValues):
        threading.Thread(target=self.__brainAreas[parNo], args=inputValues).start()