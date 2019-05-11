from Classes.Brain import Brain
from Classes.BrainArea import BrainArea
from Classes.Layer import Layer
from Classes.Neuron import Neuron
from Classes.Connection import Connection
from uuid import uuid4



def main():

    brain = Brain('Tom')

    brainArea = BrainArea('Test')

    layer0 = Layer(0)
    layer1 = Layer(1)
    layer2 = Layer(2)

    neuron00 = Neuron(0)
    neuron01 = Neuron(0)
    neuron02 = Neuron(0)
    neuron10 = Neuron(1)
    neuron11 = Neuron(1)
    neuron12 = Neuron(1)
    neuron20 = Neuron(2)
    neuron21 = Neuron(2)
    neuron22 = Neuron(2)

    layer0.AddNeuron(neuron00)
    layer0.AddNeuron(neuron01)
    layer0.AddNeuron(neuron02)
    layer1.AddNeuron(neuron10)
    layer1.AddNeuron(neuron11)
    layer1.AddNeuron(neuron12)
    layer2.AddNeuron(neuron20)
    layer2.AddNeuron(neuron21)
    layer2.AddNeuron(neuron22)

    connection0010 = Connection(neuron00, neuron10)
    connection0011 = Connection(neuron00, neuron11)
    connection0012 = Connection(neuron00, neuron12)
    connection0110 = Connection(neuron01, neuron10)
    connection0111 = Connection(neuron01, neuron11)
    connection0112 = Connection(neuron01, neuron12)
    connection0210 = Connection(neuron02, neuron10)
    connection0211 = Connection(neuron02, neuron11)
    connection0212 = Connection(neuron02, neuron12)
    connection1020 = Connection(neuron10, neuron20)
    connection1021 = Connection(neuron10, neuron21)
    connection1022 = Connection(neuron10, neuron22)
    connection1120 = Connection(neuron11, neuron20)
    connection1121 = Connection(neuron11, neuron21)
    connection1122 = Connection(neuron11, neuron22)
    connection1220 = Connection(neuron12, neuron20)
    connection1221 = Connection(neuron12, neuron21)
    connection1222 = Connection(neuron12, neuron22)

    brainArea.AddLayer(layer0)
    brainArea.AddLayer(layer1)
    brainArea.AddLayer(layer2)

    brain.AddBrainArea(brainArea)

    print(str(brain))
    return

if __name__ == '__main__': main()