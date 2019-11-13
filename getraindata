import datetime
import requests

R = requests.get("https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode=39.95%2C-75.12&language=en-US&units=e")

R = R.json()
rainAmt = R["vt1dailyForecast"]["day"]["precipAmt"]
rainPer = R["vt1dailyForecast"]["day"]["precipPct"]
temp = R["vt1dailyForecast"]["day"]["temperature"]


print(rainAmt)
print(rainPer)
print(temp)
