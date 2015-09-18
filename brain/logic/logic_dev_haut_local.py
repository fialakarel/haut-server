#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2.0

if data["key"] == "status":
    if data["value"] == "login":
        self._send("pir-18")

elif data["key"] == "temp1":
    if data["value"] > 25:
        print("IFTTT_h: too high temperature")
        self._send("dev-cool")

elif data["key"] == "pir-18":
    if data["value"] == 1:
        self._send("gpio-17-fadein")
    else:
        self._send("gpio-17-fadehalf")
        time.sleep(5)
        self._send("gpio-17-fadeout")
else:
        pass