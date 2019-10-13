from .Neuron import Neuron
from .Connection import Connection
from .Functions import activationFunctions
from random import randint
from .Helper import GetRandomFunction

class Layer(object):

    def __init__(self, parLevel, parFunction=None):
        self.__neurons = {}
        self.__level = 0
        self.__function = None
        self.__level = parLevel
        if not parFunction:
            #parFunction = GetRandomFunction()
            parFunction = activationFunctions[0]
        self.__function = parFunction


    def __str__(self):
        tempString = ''
        for neuron in self.__neurons:
            tempString += ';' + str(neuron)
        return tempString

    def GetAllNeurons(self):
        return self.__neurons

    def AddNeuron(self, neuron=None):
        if not neuron: 
            neuron = Neuron(self.__level,parFunction=self.__function)
        else:
            neuron.SetLayerLevel(self.__level)
            neuron.SetFunction(self.__function)
        
        self.__neurons[str(neuron)] = neuron

    def GetFunction(self):
        return self.__function

    def SetFunction(self,parFunction):
        self.__function = parFunction
        for _key, neuron in self.__neurons.items():
            neuron.SetFunction(parFunction)

    def GetLevel(self):
        return self.__level

    def SetLevel(self, parLevel):
        self.__level = parLevel

    def RemoveNeuron(self, neuron):
        if str(neuron) in self.__neurons:
            del self.__neurons[str(neuron)]

    def ConnectToLayer(self, parConnectToLayer):
        for _fromKey, fromNeuron in self.GetAllNeurons().items():
            for _toKey, toNeuron in parConnectToLayer.GetAllNeurons().items():
                Connection(fromNeuron, toNeuron)

    def RemoveOutputConnections(self):
        for _key, neuron in self.GetAllNeurons().items():
            neuron.RemoveAllOutputConnections()

    def RemoveInputConnections(self):
        for _key, neuron in self.GetAllNeurons().items():
            neuron.RemoveAllInputConnections()

    def RebuildConnections(self):
        self.RemoveInputConnections()
        self.RemoveOutputConnections()

        self.ConnectToLayer(self.__level - 1)
        self.ConnectToLayer(self.__level + 1)

