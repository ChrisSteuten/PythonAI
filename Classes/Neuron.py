from .Functions import activationFunctions
from .Helper import WeightedSum
from random import randint
from time import sleep
from uuid import uuid4
import threading
from .Settings import extendedDebugging

class Neuron(object):

    def __init__(self, parLayerLevel, parFunction, parID=None):
        self.__inputConnections = []
        self.__outputConnections = []
        self.__layerLevel = 0
        self.__id = 0
        self.__value = 0
        self.__expectedValue = 0
        self.__function = None
        self.__layerLevel = parLayerLevel
        self.__function = parFunction
        
        if not parID: parID = uuid4()
        self.__id = parID

    def __str__(self):
        return str(self.__layerLevel) + '.' + str(self.__id)

    def Activate(self):
        thread = threading.Thread(target=self.__Activate)
        thread.start()
        thread.join()
        

    def __Activate(self):
        if extendedDebugging:
            print('Activated ' + str(self))
        if not self.AllInputConnectionsTriggered():
            return

        if self.__layerLevel > 0:
            if len(self.__outputConnections) > 0:
                self.__value = self.__function(WeightedSum(self.__inputConnections))
            else:
                self.__value = WeightedSum(self.__inputConnections)

        for connection in self.__outputConnections:
            connection.SetValue(self.__value)
            connection.SetTriggered(True)
    
    def GetLayerLevel(self):
        return self.__layerLevel

    def SetLayerLevel(self, parLayerLevel):
        self.__layerLevel = parLayerLevel

    def GetID(self):
        return self.__id

    def SetID(self, parID):
        self.__id = parID

    def GetFunction(self):
        return self.__function

    def SetFunction(self, parFunction):
        self.__function = parFunction

    def GetValue(self):
        return self.__value

    def SetValue(self, parValue):
        self.__value = parValue

    def GetExpectedValue(self):
        return self.__expectedValue

    def SetExpectedValue(self, parValue):
        self.__expectedValue = parValue

    def AddOutputConnection(self, parOutputConnection):
        self.__outputConnections.append(parOutputConnection)

    def GetOutputConnection(self, parNo):
        return self.__outputConnections[parNo]

    def GetAllOutputConnections(self):
        return self.__outputConnections

    def RemoveAllOutputConnections(self):
        self.__outputConnections = []  


    def AddInputConnection(self, parInputConnection):
        self.__inputConnections.append(parInputConnection)

    def GetInputConnection(self, parNo):
        return self.__inputConnections[parNo]

    def GetAllInputConnections(self):
        return self.__inputConnections

    def RemoveAllInputConnections(self):
        self.__inputConnections = []  


    def AllInputConnectionsTriggered(self):
        for connection in self.__inputConnections:
            if not connection.GetTriggered():
                return False

        return True

    def TriggerOutputConnections(self):
        for connection in self.__outputConnections:
            connection.SetTriggered(True)
        
        
