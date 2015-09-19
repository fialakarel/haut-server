#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# commands


# testing
#self.setcmd("dev.haut.local", "temp", "temp.py", "")
#self.setcmd("dev.haut.local", "temp2", "temperaturex.py", "5 5")
#self.setcmd("dev.haut.local", "dev-cool", "cool.py", "")
#self.setcmd("dev.haut.local", "dev-cool2", "cool2.py", "aaa")


# real
self.setcmd("dev.haut.local", "temperature", "temperature", "28-000005e6d5be")
self.setcmd("dev.haut.local", "pir-18", "pir", "18")
#self.setcmd("dev.haut.local", "gpio-17-on", "gpio.py", "17 1")
#self.setcmd("dev.haut.local", "gpio-17-off", "gpio.py", "17 0")
self.setcmd("dev.haut.local", "gpio-17-on", "blaster", "17 0.2")
self.setcmd("dev.haut.local", "gpio-17-fadein", "fade", "17 0 0.8")

self.setcmd("dev.haut.local", "gpio-17-half", "blaster", "17 0.25")

self.setcmd("dev.haut.local", "gpio-17-off", "blaster", "17 0")
self.setcmd("dev.haut.local", "gpio-17-fadeout", "fade", "17 0.2 0")

self.setcmd("dev.haut.local", "gpio-17-fadehalf", "fade", "17 0.8 0.2")

self.setcmd("dev.haut.local", "dev-status", "status", "")


self.setcmd("bedroom1.haut.local", "bedroom1-status", "status", "")
self.setcmd("bedroom1.haut.local", "bedroom1-temp1", "temperature", "28-000006dc1ec1")
self.setcmd("bedroom1.haut.local", "heatbed-on", "gpio", "17 1")
self.setcmd("bedroom1.haut.local", "heatbed-off", "gpio", "17 0")

