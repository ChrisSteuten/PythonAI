from .Neuron import Neuron

class Layer(object):
    __neurons = {}
    __level = 0

    def __init__(self, parLevel):
        self.__level = parLevel

    def __str__(self):
        tempString = ''
        for neuron in self.__neurons:
            tempString += ';' + str(neuron)
        return tempString

    def GetAllNeurons(self):
        return self.__neurons

    def AddNeuron(self, neuron=None):
        if not neuron: neuron = Neuron(self.__level)
        neuron.SetLayerLevel(self.__level)
        self.__neurons[str(neuron)] = neuron

    def RemoveNeuron(self, neuron):
        if str(neuron) in self.__neurons:
            del self.__neurons[str(neuron)]