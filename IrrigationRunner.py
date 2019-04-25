# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:00:10 2018

@author: Justin
"""

import logic.py as logic

import RPi.GPIO as GPIO
from board import SCL, SDA
import busio
import time

from adafruit_seesaw.seesaw import Seesaw

#create objects
moisture_logic = logic()
i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)

#set up pi
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
    touch = ss.moisture_read()
    shouldWater = logic.evaluate_logic(None, touch)

    print("Moisture: " + str(touch) + ". Should water?" + str(shouldWater))
    
    if shouldWater:
        GPIO.output(17, 0)
    else:
        GPIO.output(17, 1)
        
    time.sleep(1)