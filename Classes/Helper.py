import threading

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