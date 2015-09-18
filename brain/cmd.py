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
        exec(open("./brain/logic/cmds.py").read())

    
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
    
