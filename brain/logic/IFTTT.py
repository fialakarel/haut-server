#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2.0

logic_webserver_haut_local = open("./brain/logic/logic_webserver_haut_local.py").read()
logic_dev_haut_local = open("./brain/logic/logic_dev_haut_local.py").read()

if host == "dev.haut.local":
    exec(logic_dev_haut_local)


elif host == "dev2.haut.local":
    pass


elif host == "webserver.haut.local":
    exec(logic_webserver_haut_local)

else:
    pass

