#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2.0

import os,sys,time
from network import Network
from .cmd import Cmd
from .mem import Mem

import socket
from datetime import datetime


class Brain(object):
    
    def __init__(self):
        self.mem = Mem()
        self.cmd = Cmd()
        self.net = Network()
        
        self.ifttt = open("./brain/logic/IFTTT.py").read()
        
        pass
    
    def process(self, data, ip):
        # process request from client
        print(str(datetime.now()) + " " + str(self.net.gethost(ip[0])) + ":" + str(ip[1]) + " " + str(data))
        self.mem.setmem(str(self.net.gethost(ip[0])) + "_" + str(data["key"]), str(data["value"]))
        
        host=str(self.net.gethost(ip[0]))        
        
        # if this than this
        exec(self.ifttt)


    def run(self):
        # create requests for clients
        
        # run these at startup
        exec(open("./brain/logic/ServerStartup.py").read())
        
        # run these forever code -- optimization
        period=open("./brain/logic/Periodical.py").read()
        
        while True:
            # run these forever
            exec(period)


    def _send(self, cmd):
        tmp = self.cmd.getcmd(cmd)
        self.net.send(tmp, tmp["dev"], 5555)
        
