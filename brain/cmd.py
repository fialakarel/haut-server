#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# commands


class Cmd(object):
    
    def __init__(self):
        # initialization
        self.cmd = dict()
        self.createcmds()
    
    def createcmds(self):
        # testing
        self.setcmd("dev.haut.local", "temp", "temp.py", "")
        self.setcmd("dev.haut.local", "temp2", "temperaturex.py", "5 5")
        self.setcmd("dev.haut.local", "dev-cool", "cool.py", "")
        self.setcmd("dev.haut.local", "dev-cool2", "cool2.py", "aaa")
        
        # real
        self.setcmd("dev.haut.local", "temperature", "temperature.py", "28-000005e6d5be")
        self.setcmd("dev.haut.local", "pir-18", "pir.py", "18")
        self.setcmd("dev.haut.local", "gpio-17-on", "gpio.py", "17 1")
        self.setcmd("dev.haut.local", "gpio-17-off", "gpio.py", "17 0")
        self.setcmd("dev.haut.local", "dev-status", "status.py", "")
    
    def getcmd(self, key):
        return self.cmd[key]
    
    def setcmd(self, dev, key, cmd, arg=""):
        # create cmd
        x = dict()
        x["cmd"] = cmd
        x["arg"] = arg
        x["dev"] = dev

        # register cmd
        self.cmd[key] = x
    
