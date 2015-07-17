#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.1.2

import os,sys,time
from network import Network
from .cmd import Cmd
from .mem import Mem

import socket


class Brain(object):
    
    def __init__(self):
        self.mem = Mem()
        self.cmd = Cmd()
        self.net = Network()
        pass
    
    def process(self, d):
        # process request from client
        print(d)
        pass
    
    def run(self):
        # create requests for clients
        while True:
            self._send("temp")
            time.sleep(5)




    def _send(self, cmd):
        tmp = self.cmd.getcmd(cmd)
        self.net.send(tmp, tmp["dev"], 5555)
        
