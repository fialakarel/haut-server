#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2.0


import threading
from config import *
from network import Network
from brain.brain import Brain
import sys

# ======================

# create brain
global brain
brain = Brain()

# start listening
udp = Network("0.0.0.0", SERVER_PORT)

# ======================

def reqrecv():
    #global udp
    try:
        while True:
            d = udp.recv()
            ip = udp.recv_from()
            (threading.Thread(target=brain.process, args=(d,ip))).start()

    except KeyboardInterrupt:
        sys.exit(0)
    return


# receive requests from clients
try:
    (threading.Thread(target=reqrecv)).start()
except KeyboardInterrupt:
    sys.exit(0)

# ======================

# create requests for clients
try:
    (threading.Thread(target=brain.run)).start()
except KeyboardInterrupt:
    sys.exit(0)

# ======================

print("Running ...")