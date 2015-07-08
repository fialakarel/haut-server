#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2

import sys
from config import *
from network import Network
from brain.commands import *

udp = Network()

try:
    while True:
        in1 = input("[haut-server] cmd/raw: ")
        if in1 == "cmd":
            for key in cmd:
                print(key)
            in2 = input("[haut-server] CMD: ")
            try:
                udp.send(cmd[in2], "127.0.0.1", 5555)
            except:
                print("ERR")
            continue

        elif in1 == "raw":
            d = dict()
            d["cmd"] = input("[haut-server] CMD: ")
            d["arg"] = input("[haut-server] ARG: ")
            while True:
                other = input("[haut-server] other [y/n]: ")
                if other == "y":
                    key1 = input("[haut-server] KEY: ")
                    d[key1] = input("[haut-server] VALUE: ")
                elif other == "n":
                    break
                else:
                    continue
            udp.send(d, "127.0.0.1", 5555)
            continue

        else:
            continue
        
        
except KeyboardInterrupt:
    sys.exit(0)
