from .Layer import Layer
import threading
from time import sleep

class BrainArea(object):
    __layers = []
    __purpose = ''
    __isWorking = False

    def __init__(self,parPurpose=''):
        self.__purpose = parPurpose

    def __str__(self):
        tempString = ''
        for layer in self.__layers:
            tempString += '+' + str(layer)
        return tempString

    def GetAllNeurons(self):
        tempNeuronList = []
        for layer in self.__layers:
            tempNeuronList.extend(layer.GetAllNeurons())
        return tempNeuronList

    def GetNeuronsOfLayer(self, parLayer):
        self.__layers[parLayer].GetAllNeurons()  

    def AddLayer(self, parLayer=None):
        if not parLayer: parLayer = Layer(len(self.__layers))
        self.__layers.append(parLayer)

    def RemoveLayer(self, parLevel):
        del self.__layers[parLevel]

    def GetLayer(self, parLevel):
        if parLevel < 0:
            return

        if parLevel > len(self.__layers):
            return

        return self.__layers[parLevel]

    def Activate(self, inputValues):
        if self.__isWorking:
            return
        
        self.__isWorking = True

        threads = []
        counter = 0
        for neuron in self.__layers[0].GetAllNeurons():
            threads.append(threading.Thread(target=neuron.Activate, args=inputValues[counter]))
            counter += 1

        for thread in threads:
            thread.start()

        for thread in threads:
            if thread.isAlive():
                thread.join()

        self.ResetConnectionsTriggerStatus()

        self.__isWorking = False

    def ResetConnectionsTriggerStatus(self):
        for layer in self.__layers:
            for neuron in layer.GetAllNeurons():
                for connection in neuron.GetAllOutputConnections():
                    connection.SetTriggered(False)

                for connection in neuron.GetAllInputConnections():
                    connection.SetTriggered(False)

        