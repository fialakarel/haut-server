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
        pass
    
    def process(self, data, ip):
        # process request from client
        print(str(datetime.now()) + " " + str(self.net.gethost(ip[0])) + ":" + str(ip[1]) + " " + str(data))
        self.mem.setmem(str(self.net.gethost(ip[0])) + "_" + str(data["key"]), str(data["value"]))
        
        # debug
        #self.mem.printall()
        
        # if this than this
        self.ifttt(data, str(self.net.gethost(ip[0])))
    
    
    
    def ifttt(self, data, host):
        if host == "dev.haut.local":
            if data["key"] == "status":
                if data["value"] == "login":
                    self._send("pir-18")
                
            elif data["key"] == "temp1":
                if data["value"] > 25:
                    print("IFTTT_h: too high temperature")
                    self._send("dev-cool")
            elif data["key"] == "pir-18":
                if data["value"] == 1:
                    self._send("gpio-17-on")
                else:
                    self._send("gpio-17-off")
            else:
                    pass

        elif host == "dev2.haut.local":
            pass
        
        elif host == "webserver.haut.local":
            if data["key"] == "get":
                d = self.mem.getmem(data["value"])
                self.net.send(d, "webserver.haut.local", 5557)
            
            if data["key"] == "set":
                self._send(data["value"])
        
        else:
            pass
    
    
    
    def ifttt_period(self):
        if int(self.mem.getmem("dev.haut.local_temp1")) > 28:
                print("IFTTT_p: blabla")
                self._send("dev-cool2")



    def run(self):
        # create requests for clients
        self._send("pir-18")
        while True:
            self._send("temperature")
            self._send("dev-status")
            time.sleep(5)
            self.ifttt_period()




    def _send(self, cmd):
        tmp = self.cmd.getcmd(cmd)
        self.net.send(tmp, tmp["dev"], 5555)
        
