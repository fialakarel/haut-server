#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.0.2


class Mem(object):
    
    def __init__(self):
        # initialization
        self.mem = dict()

    def setmem(self, key, value):
        self.mem[key.replace('.','-')] = value
        
    def getmem(self, key):
        try:
            return self.mem[key.replace('.','-')]
        except KeyError:
            return False
    
    def printall(self):
        for key,value in self.mem.items():
            print(str(key) + ": " + str(value))
    