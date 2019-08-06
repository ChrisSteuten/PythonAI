import threading
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

def GetNumBeforePoint(x):
    s = str(x)
    if not '.' in s:
        return len(s)

    return s.index('.') - 1
    
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