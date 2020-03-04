from datetime import date
import requests
import time
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw
import RPi.GPIO as GPIO


#Moisture sensor ranges from 200 (very dry) to 2000 (very wet)
opt_level_to_maintain = 700
base_level_to_maintain = 700
weather_data = None
enough_water_gathered = none
shed_sqr_inch = 3456
threshRain = None
waterGainThresh = None

def set_sensors():
    i2c_bus = busio.I2C(SCL, SDA)
    ss = Seesaw(i2c_bus, addr=0x36)
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    return ss

def get_weather():
    R = requests.get("https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode=39.95%2C-75.12&language=en-US&units=e") 
    R = R.json()
    rainAmt = R["vt1dailyForecast"]["day"]["precipAmt"]
    rainPer = R["vt1dailyForecast"]["day"]["precipPct"]
    temp = R["vt1dailyForecast"]["day"]["temperature"]
    return (rainAmt,rainPer,temp)
  
#Water for the next three days in gallons
def calc_additional_water(weather_data):
    rain_amt = weather_data[0]
    predRain = rainAmt[0] + rainAmt[1] + rainAmt[2]  #gets next 3 days of predicted rain
    amt = predRain*shed_sqr_inch
    #convert square inches into gallons
    amt = amt / 231
    return amt

def evaluate_logic(weather_data,water_level):
    rainAmt = weather_data[0]
    expected_water_gain = calc_additional_water(weather_data) #Expected gain of water in gallons
    if weather_data is not None:
        amt_rain = rainAmt[0] #The amount of rain for today
    else:
        amt_rain = -1
    if amt_rain > 1:        #Yes Raining
        if water_level > base_level_to_maintain: #check amt
            if water_level > optimal_level_to_maintain:
                return False
            else:
                if expected_water_gain > waterGainThresh:
                    return True
                else:
                 return False
        else:
            if rainAmnt > threshRain:
                return False
            else:
                return True     
                            
    else: #Right side of tree
        if water_level > base_level_to_maintain:
            if water_level > optimal_level_to_maintain:
                return False
            else:
                if expected_water_gain > waterGainThresh:
                    return True
                else:
                 return False
        else:
            return True              
 
def runner():
    day = date.today()
    ss = set_sensors()
    weather_data = get_weather()
    While True:
        water_level = ss.moisture_read()
        if day != date.today() #New Day:
            weather_data = get_weather()
            day = date.today()
       if evaluate_logic(weather_data,water_level):
           GPIO.output(17, 1)
       else:
           GPIO.output(17, 0)
