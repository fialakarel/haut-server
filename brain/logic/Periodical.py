#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2.0

self._send("temperature")
self._send("dev-status")

self._send("bedroom1-temp1")
self._send("bedroom1-status")


if int(self.mem.getmem("dev.haut.local_temp1")) > 28:
    print("IFTTT_p: blabla")
    self._send("dev-cool2")

time.sleep(5)
