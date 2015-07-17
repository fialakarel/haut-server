#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2.0


import threading
from config import *
from network import Network
from brain.brain import Brain

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
            (threading.Thread(target=brain.process, args=(d,))).start()

    except KeyboardInterrupt:
        pass
    return


# receive requests from clients
(threading.Thread(target=reqrecv)).start()

# ======================

# create requests for clients
(threading.Thread(target=brain.run)).start()

# ======================

print("Running ...")