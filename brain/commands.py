#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# commands

cmd = dict()

d1 = dict()
d1["cmd"] = "led.py"
d1["arg"] = "gpio4 0 gpio5 100 gpio6 100"

cmd["led-on"] = d1


d2 = dict()
d2["cmd"] = "temp.py"

cmd["temp"] = d2


d3 = dict()
d3["cmd"] = "temperature.py"
d3["arg"] = "5 5"

cmd["temp2"] = d3