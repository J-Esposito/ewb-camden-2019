import time
import RPi.GPIO as GPIO
from board import SCL, SDA
import busio

#Pin 9 is 17, not 0


from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()

    # read temperature from the temperature sensor
    temp = ss.get_temp()

    print("temp: " + str(temp) + "  moisture: " + str(touch))
    
    if touch < 700:
        GPIO.output(17, 0)
    else:
        GPIO.output(17, 1)
        
    time.sleep(1)
