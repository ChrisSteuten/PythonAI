import threading
from math import ceil, trunc
from .Functions import activationFunctions
from random import randint


def AllThreadsStopped(parThreadList):
    for thread in parThreadList:
        if thread.isAlive():
            return False
            
        return True

def WeightedSum(parConnectionList):
    tempFloat = 0.0
    for connection in parConnectionList:
        tempFloat += (connection.GetValue() * connection.GetWeight())
    return tempFloat

def GetRandomFunction():
    return activationFunctions[randint(0, len(activationFunctions) - 1)]

def GetFirstFunction():
    return activationFunctions[0]

def GetNextFunction(currentFunction):
    currentFunctionIndex = activationFunctions.index(currentFunction)
    if currentFunctionIndex < len(activationFunctions) - 1:
        return activationFunctions[currentFunctionIndex + 1]
    
    return None

def GetNumBeforePoint(x):
    s = str(x)
    s = s.replace('-', '')
    
    if not '.' in s:
        return len(s)

    return s.index('.')
    
def GetZeroAfterPoint(x):
    s = str(x)
    if not '.' in s:
        return 0
    
    count = 0

    currentIndex = s.index('.') + 1
    while currentIndex < len(s):
        if s[currentIndex] == '0':
            count += 1
            currentIndex += 1
        else:
            return count

    return count

def RoundUp(number, decimals=0):
    multiplier = 10 ** decimals
    return(ceil(number + multiplier) / multiplier)

def truncate(number):
    return(trunc(number))



