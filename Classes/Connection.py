from .Neuron import Neuron
from random import uniform

class Connection(object):
    __value = 0.0
    __weight = 0.0
    __from = Neuron
    __to = Neuron
    __triggered = False

    def __init__(self, parFrom, parTo, parWeight=None):
        self.__from = parFrom
        self.__to = parTo
        if not parWeight: parWeight = uniform(-1,1)
        self.__weight = parWeight

        parFrom.AddOutputConnection(self)
        parTo.AddInputConnection(self)

    def __str__(self):
        return str(self.__from) + ':' + str(self.__to)

    def SetWeight(self, parWeight):
        self.__weight = parWeight

    def GetWeight(self):
        return self.__weight

    def SetValue(self, parValue):
        self.__value = parValue

    def GetValue(self):
        return self.__value

    def GetFromNeuron(self):
        return self.__from

    def GetToNeuron(self):
        return self.__to

    def SetTriggered(self, parValue):
        self.__triggered = parValue

    def GetTriggered(self):
        return self.__triggered