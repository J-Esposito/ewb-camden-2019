import datetime
import requests

#Moisture sensor ranges from 200 (very dry) to 2000 (very wet)
opt_level_to_maintain = 700
base_level_to_maintain = 700
weather_data = None
enough_water_gathered = none
shed_sqr_inch = 3456
threshRain = None
waterGainThresh = None



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
            return False
        else:
            if rainAmnt > threshRain:
                return False
            else:
                if expected_water_gain > waterGainTresh
                    if waterlevel < opt_level_to_maintain:
                        return True
                    else:
                        return False
                else:
                    if waterlevel < base_level_to_maintain:
                        return True
                    else:
                        return False
                 
    else: #Right side of tree
        if water_level > base_level_to_maintain:
            return False
        else:
            if expected_water_gain < waterGainThresh #checking if there is enough water to water to opt amt
                if waterlevel < base_level_to_maintain:
                    return True
                else:
                    return False
            else
                if water_level < opt_level_to_maintain
                    return true
                else
                    return false 
                   
                
 
def runner():
    While True:
        if #New Day:
            #Get New Weather Data
            weather_data = get_weather()
        evaluate_logic(weather_data,water_level)
           
