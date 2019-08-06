import threading
import json
from .BrainArea import BrainArea

class Brain(object):

    def __init__(self,parName):
        self.__name = ''
        self.__brainAreas = []
        self.__name = parName

    def __str__(self):
        tempString = self.__name
        for brainArea in self.__brainAreas:
            tempString += '/' + str(brainArea)
        return tempString

    def GetBrainAreas(self):
        return self.__brainAreas

    def GetBrainArea(self, key):
        return self.__brainAreas[key]

    def GetAllBrainAreas(self):
        return self.__brainAreas

    def GetBrainAreasCount(self):
        return len(self.__brainAreas)

    def AddBrainArea(self, parBrainArea=None):
        if not parBrainArea: parBrainArea = BrainArea()
        self.__brainAreas.append(parBrainArea)

    def GetAllNeurons(self):
        tempNeuronTable = {}
        for brainArea in self.__brainAreas:
            tempNeuronTable = {**tempNeuronTable, **brainArea.GetAllNeurons()}
        return tempNeuronTable

    def ActivateBrainArea(self, parNo, inputValues):
        threading.Thread(target=self.__brainAreas[parNo], args=inputValues).start()