#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2.0

if data["key"] == "get":
    d = self.mem.getmem(data["value"])
    self.net.send(d, "webserver.haut.local", 5557)

if data["key"] == "set":
    self._send(data["value"])
