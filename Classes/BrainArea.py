from .Layer import Layer
import threading
from time import sleep
from math import isnan, isinf
from .Helper import GetRandomFunction, GetZeroAfterPoint, GetNumBeforePoint
from .Settings import extendedDebugging

class BrainArea(object):

    def __init__(self,parPurpose=''):
        self.__layers = []
        self.__purpose = ''
        self.__isWorking = False
        self.__purpose = parPurpose
        self.__oldAverages = None
        self.__functionShuffleCount = 0

    def __str__(self):
        tempString = ''
        for layer in self.__layers:
            tempString += '+' + str(layer)
        return tempString

    def GetAllNeurons(self):
        tempNeuronTable = {}
        for layer in self.__layers:
            tempNeuronTable = {**tempNeuronTable, **layer.GetAllNeurons()}
        return tempNeuronTable

    def GetNeuronsOfLayer(self, parLayer):
        self.__layers[parLayer].GetAllNeurons()  

    def AddLayer(self, parLayer=None):
        if not parLayer: parLayer = Layer(len(self.__layers))
        self.__layers.append(parLayer)

    def AddHiddenLayer(self):
        outputLayer = self.GetOutputLayer()
        outputLayer.RemoveInputConnections()
        
        newLayer = Layer(outputLayer.GetLevel())
        outputLayer.SetLevel(outputLayer.GetLevel() + 1)
        
        i = 0
        while i < len(self.GetInputLayer().GetAllNeurons()):
            newLayer.AddNeuron()
            i += 1

        previousLayer = self.GetLayer(newLayer.GetLevel() - 1)
        previousLayer.RemoveOutputConnections()

        previousLayer.ConnectToLayer(newLayer)
        newLayer.ConnectToLayer(outputLayer)

        self.RemoveLayer(newLayer.GetLevel())
        self.AddLayer(newLayer)
        self.AddLayer(outputLayer)

    def RemoveLayer(self, parLevel):
        del self.__layers[parLevel]

    def SetLayer(self,parLayer):
        self.__layers[parLayer.GetLevel()] = parLayer

    def GetLayer(self, parLevel):
        if parLevel < 0:
            return

        if parLevel > len(self.__layers):
            return

        return self.__layers[parLevel]

    def GetInputLayer(self):
        return self.GetLayer(0)

    def GetOutputLayer(self):
        return self.GetLayer(len(self.GetAllLayers()) - 1)

    def GetAllLayers(self):
        return self.__layers

    def GetOutputPrediction(self, inputValues):
        counter = 0
        for key, neuron in self.GetInputLayer().GetAllNeurons().items():
            neuron.SetValue(inputValues[counter])
            counter += 1
        
        predictions = []
        for key, neuron in self.GetOutputLayer().GetAllNeurons().items():
            currPrediction = 0.0
            for connection in neuron.GetAllInputConnections():
                currPrediction += connection.GetOutputPrediction()
                
            predictions.append(currPrediction)

        return predictions

    def Activate(self, inputValues):
        if self.__isWorking:
            return
        
        self.__isWorking = True

        #threads = []
        counter = 0
        for key, neuron in self.GetInputLayer().GetAllNeurons().items():
            neuron.SetValue(inputValues[counter])
            neuron.Activate()
            counter += 1

        self.ResetConnectionsTriggerStatus()

        self.__isWorking = False

    def Optimize(self, outputValues, expectedOutputValues, results):
        errors = [] 
        newLearningRate = 1
        if outputValues != expectedOutputValues:
            results.append(outputValues)
            print('Output Values: ' + str(outputValues).strip('[]'))

            #Calculate error
            expectedAndActualOutputValues = zip(expectedOutputValues, outputValues)
            for expectedValue, actualValue in expectedAndActualOutputValues:
                errors.append(expectedValue - actualValue)
                
                newLearningRate = 1

                if (newLearningRate == 1):
                    zerosAfterDecimalPointCount = GetZeroAfterPoint(expectedValue - actualValue)
                    i = 0

                    if zerosAfterDecimalPointCount > 0:
                        newLearningRate /= 10
                        while i < zerosAfterDecimalPointCount:
                            newLearningRate /= 10
                            i += 1

                learningRate = newLearningRate           

            if extendedDebugging:
                print('Errors: ' + str(errors).strip('[]'))

            for layer in self.GetAllLayers():
                for key, neuron in layer.GetAllNeurons().items():
                    for connection in neuron.GetAllInputConnections():
                        currWeight = connection.GetWeight()
                        currValue = connection.GetValue()
                        inputPrediction = connection.GetInputPrediction()
                        outputPrediction = connection.GetOutputPrediction()

                        newWeight = currWeight - learningRate * (outputPrediction - currValue) * inputPrediction

                        if isnan(newWeight) or isinf(newWeight):
                            print('nan!')

                        connection.SetWeight(newWeight)

            lastHundredResults = results[-100:]

            if len(lastHundredResults) == 100:

                averages = [float(sum(col))/len(col) for col in zip(*lastHundredResults)]
                firstLastHundredResults = lastHundredResults[0]
                lastLastHundredResults = lastHundredResults[-1]

                if ((not averages != self.__oldAverages) and (firstLastHundredResults == lastLastHundredResults)) or (isnan(lastLastHundredResults[0]) or isinf(lastLastHundredResults[0])):
                    if self.__functionShuffleCount < len(self.GetAllLayers()):
                        self.ShuffleFunctions()
                        self.__oldAverages = None
                    else:
                        self.__functionShuffleCount = 0
                        self.__oldAverages = None
                        self.AddHiddenLayer()

                self.__oldAverages = averages
        return results


    def ResetConnectionsTriggerStatus(self):
        for layer in self.__layers:
            for key, neuron in layer.GetAllNeurons().items():
                for connection in neuron.GetAllOutputConnections():
                    connection.SetTriggered(False)

                for connection in neuron.GetAllInputConnections():
                    connection.SetTriggered(False)

    def ShuffleFunctions(self):
        self.__functionShuffleCount += 1
        for layer in self.GetAllLayers():
            layer.SetFunction(GetRandomFunction())

        