from .Functions import activationFunctions
from .Helper import WeightedSum
from random import randint
from time import sleep
from uuid import uuid4

class Neuron(object):
    __inputConnections = []
    __outputConnections = []
    __layerLevel = 0
    __id = 0

    def __init__(self, parLayerLevel, parID=None):
        self.__function = activationFunctions[randint(0, len(activationFunctions) - 1)]
        self.__layerLevel = parLayerLevel
        
        if not parID: parID = uuid4()
        self.__id = parID

    def __str__(self):
        return str(self.__layerLevel) + '.' + str(self.__id)

    def Activate(self):
        while not self.AllInputConnectionsTriggered():
            sleep(0.01)
        
        self.__function(WeightedSum(self.__inputConnections))

    
    def GetLayerLevel(self):
        return self.__layerLevel

    def SetLayerLevel(self, parLayerLevel):
        self.__layerLevel = parLayerLevel


    def GetID(self):
        return self.__id

    def SetID(self, parID):
        self.__id = parID


    def AddOutputConnection(self, parOutputConnection):
        self.__outputConnections.append(parOutputConnection)

    def GetOutputConnection(self, parNo):
        return self.__outputConnections[parNo]

    def GetAllOutputConnections(self):
        return self.__outputConnections


    def AddInputConnection(self, parInputConnection):
        self.__inputConnections.append(parInputConnection)

    def GetInputConnection(self, parNo):
        return self.__inputConnections[parNo]

    def GetAllInputConnections(self):
        return self.__inputConnections   


    def AllInputConnectionsTriggered(self):
        for connection in self.__inputConnections:
            if not connection.GetTriggered():
                return False

        return True

    def TriggerOutputConnections(self):
        for connection in self.__outputConnections:
            connection.SetTriggered(True)
        
        
