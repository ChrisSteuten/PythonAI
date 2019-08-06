import math
import threading
from .Settings import extendedDebugging

def WeightedSum(inputConnectionsList = []):
    if extendedDebugging:
        print('\n' + threading.currentThread().getName() + ' Run WeightedSum with ' + str(inputConnectionsList))
    tempFloat = 0.0
    for element in inputConnectionsList:
        tempFloat = tempFloat + (element.GetValue() * element.GetWeight())
    if extendedDebugging:
        print(threading.currentThread().getName() + ' Exit WeightedSum with ' + str(tempFloat) + '\n')
    return tempFloat

def DummyFunction(inputFloat = 0):
    if extendedDebugging:
        print('\n' + threading.currentThread().getName() + ' Run DummyFunction with ' + str(inputFloat))
    if extendedDebugging:
        print(threading.currentThread().getName() + ' Exit DummyFunction with ' + str(inputFloat) + '\n')
    return inputFloat

def RELU(inputFloat = 0):
    if extendedDebugging:
        print('\n' + threading.currentThread().getName() + ' Run RELU with ' + str(inputFloat))
    if inputFloat < 0:
        inputFloat = 0

    if extendedDebugging:
        print(threading.currentThread().getName() + ' Exit RELU with ' + str(inputFloat) + '\n')
    return inputFloat

def LogisticFunction(inputFloat = 0):
    if extendedDebugging:
        print('\n' + threading.currentThread().getName() + ' Run LogisticFunction with ' + str(inputFloat))

    res = (1 / (1 + math.e - inputFloat))

    if extendedDebugging:
        print(threading.currentThread().getName() + ' Exit LogisticFunction with ' + str(res) + '\n')   
    return res

def HyperbolicTangent(inputFloat = 0):
    if extendedDebugging:
        print('\n' + threading.currentThread().getName() + ' Run HyperbolicTangent with ' + str(inputFloat))

    res = (math.tanh(inputFloat))

    if extendedDebugging:
        print(threading.currentThread().getName() + ' Exit HyperbolicTangent with ' + str(res) + '\n')   
    return res

def ArctangentFunction(inputFloat = 0):
    if extendedDebugging:
        print('\n' + threading.currentThread().getName() + ' Run ArctangentFunction with ' + str(inputFloat))

    res = (math.atan(inputFloat))

    if extendedDebugging:
        print(threading.currentThread().getName() + ' Exit ArctangentFunction with ' + str(res) + '\n')   
    return res

def GudermannianFunction(inputFloat = 0):
    if extendedDebugging:
        print('\n' + threading.currentThread().getName() + ' Run GudermannianFunction with ' + str(inputFloat))

    res = (2 * math.atan(math.tanh(inputFloat / 2)))

    if extendedDebugging:
        print(threading.currentThread().getName() + ' Exit GudermannianFunction with ' + str(res) + '\n')   
    return res

def ErrorFunction(inputFloat = 0):
    if extendedDebugging:
        print('\n' + threading.currentThread().getName() + ' Run ErrorFunction with ' + str(inputFloat))

    res = (math.erf(inputFloat))

    if extendedDebugging:
        print(threading.currentThread().getName() + ' Exit ErrorFunction with ' + str(res) + '\n')   
    return res

activationFunctions = [
    DummyFunction,
    RELU,
    LogisticFunction,
    HyperbolicTangent,
    ArctangentFunction,
    GudermannianFunction,
    ErrorFunction
]

