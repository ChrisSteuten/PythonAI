from Classes.Brain import Brain
from Classes.BrainArea import BrainArea
from Classes.Layer import Layer
from Classes.Neuron import Neuron
from uuid import uuid4
import json
import math
import datetime
import itertools
from statistics import mean


def main1():

    brain = Brain('Tom')

    brain.AddBrainArea()
    
    for brainArea in brain.GetAllBrainAreas():

        brainArea.AddLayer()
        brainArea.AddLayer()
        #brainArea.AddLayer()

        layer0 = brainArea.GetLayer(0)
        layer1 = brainArea.GetLayer(1)
        #layer2 = brainArea.GetLayer(2)

        layer0.AddNeuron()
        layer0.AddNeuron()
        #layer0.AddNeuron()

        layer1.AddNeuron()
        #layer1.AddNeuron()
        #layer1.AddNeuron()

        #layer2.AddNeuron()
        #layer2.AddNeuron()
        #layer2.AddNeuron()

        currentLayerIndex = 0
        while currentLayerIndex < len(brainArea.GetAllLayers()) - 1:
            currentLayer = brainArea.GetLayer(currentLayerIndex)
            currentLayer.ConnectToLayer(brainArea.GetLayer(currentLayerIndex + 1))
            currentLayerIndex += 1

    print('\n')

    print('/ = Start of new brain area')
    print('+ = Start of new layer')
    print('; = Start of new neuron')

    print('\n')
    
    print('Brain:')
    print(str(brain))

    print('\n')

    print('Connections:')
    for key, neuron in brain.GetAllNeurons().items():
        for connection in neuron.GetAllOutputConnections():
            print(str(connection.GetFromNeuron()) + '-->' + str(connection.GetToNeuron()))
        print()

    currentBrainArea = brain.GetBrainArea(0)
    inputValues = [2,3]
    expectedOutputValues = [6]
    outputValues = []
    
    start = datetime.datetime.now().timestamp()

    i = 0
    for key, neuron in currentBrainArea.GetOutputLayer().GetAllNeurons().items():
        neuron.SetExpectedValue(expectedOutputValues[i])
        i += 1

    results = []
    while outputValues != expectedOutputValues:
        #Clear output values
        outputValues = []
        

        #Activate simulation
        currentBrainArea.Activate(inputValues)

        #Get output values
        for key, neuron in currentBrainArea.GetOutputLayer().GetAllNeurons().items():
            outputValues.append(neuron.GetValue())

        if outputValues != expectedOutputValues:
            results = currentBrainArea.Optimize(outputValues, expectedOutputValues, results)

    print()
    print('Runtime: ' + str(((datetime.datetime.now().timestamp() - start) * 1000)) + ' ms') 

    return

if __name__ == '__main__': 
    main1()