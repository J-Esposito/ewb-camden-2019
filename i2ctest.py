# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 20:35:29 2019

@author: Justin
"""

import time

from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

while True:
    touch = ss.moisture_read()
    temp = ss.get_temp()
    
    print(str(temp) + " " + str(touch))
    time.sleep(1)