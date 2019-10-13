from .Neuron import Neuron
from random import uniform
from math import exp
from sys import float_info

class Connection(object):

    def __init__(self, parFrom, parTo, parWeight=None):
        self.__value = 0.0
        self.__weight = 0.0
        self.__from = Neuron
        self.__from = parFrom
        self.__to = Neuron
        self.__to = parTo
        self.__triggered = False
        if not parWeight: parWeight = 0#uniform(-1,1)
        self.__weight = parWeight
        self.__originWeight = parWeight

        parFrom.AddOutputConnection(self)
        parTo.AddInputConnection(self)

    def __str__(self):
        return str(self.__from) + ':' + str(self.__to)

    def SetWeight(self, parWeight):        
        #while parWeight > 1 or parWeight < -1:
            #parWeight /= 10.

        try:
            parWeight = 1 / (1 + exp(-parWeight))
        except OverflowError:
            parWeight = 1 / float_info.max

        self.__weight = parWeight

    def GetWeight(self):
        return self.__weight

    def ResetWeight(self):
        self.__weight = self.__originWeight

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

        if parValue == True:
            self.__to.Activate()

    def GetTriggered(self):
        return self.__triggered

    def GetInputPrediction(self):       
        fromNeuron = self.GetFromNeuron()
        if len(fromNeuron.GetAllInputConnections()) == 0: #Input Neuron
            return fromNeuron.GetValue()
        
        prediction = 0.0
        for connection in fromNeuron.GetAllInputConnections():
            prediction += connection.GetOutputPrediction()

        return fromNeuron.GetFunction()(prediction)

    def GetOutputPrediction(self):       
        fromNeuron = self.GetFromNeuron()
        if len(fromNeuron.GetAllInputConnections()) == 0: #Input Neuron
            return fromNeuron.GetValue() * self.GetWeight()

        return self.GetInputPrediction() * self.GetWeight()
        