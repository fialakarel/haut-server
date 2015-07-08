#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.1.2

import os,sys,time
from network import Network
from .commands import *


class Brain(object):
    
    def __init__(self):
        # initialization
        pass
    
    def process(self, d):
        # process request from client
        print(d)
        pass
    
    def run(self):
        # create requests for clients
        net = Network()
        while True:
            net.send(cmd["led-on"], "127.0.0.1", 5555)
            time.sleep(5)
