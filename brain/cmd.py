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
        self.setcmd("dev.haut.local", "temp", "temp.py", "")
        self.setcmd("dev.haut.local", "temp2", "temperature.py", "5 5")
        self.setcmd("dev.haut.local", "dev-cool", "cool.py", "")
        self.setcmd("dev.haut.local", "dev-cool2", "cool2.py", "aaa")
    
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
    
