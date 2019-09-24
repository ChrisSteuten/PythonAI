import threading
import json
from .Settings import brainJsonPath
from .BrainArea import BrainArea
from json import JSONEncoder
import pickle

def _default(self, obj):
    return {'_python_object': pickle.dumps(obj)}

JSONEncoder.default = _default  # Replace with the above.


class Brain(object):

    def __init__(self,parName):
        self.__name = ''
        self.__brainAreas = []
        self.__name = parName
        self.ToJson()

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
        threading.Thread(target=self.__brainAreas[parNo]).join()
        self.ToJson()

    def ToJson(self, path=brainJsonPath):
        #brainJsonString = json.dumps(self, indent=4)
        file = open(path, 'wb+')
        file.seek(0)
        file.truncate()
        pickle.dump(self, file)
        #with open(path, 'r') as file:
        #    _data = file.read()
        
        #with open(path, 'w') as file:
        #    file.write(brainJsonString)