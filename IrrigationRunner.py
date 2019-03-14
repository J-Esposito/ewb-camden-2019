# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:00:10 2018

@author: Justin
"""

import json
import pprint

f = open("sample_data.json")

weather_data = json.load(f)
for x in weather_data['list']:
    pprint.pprint(x)
    
#weather_data = weather_data['list'][1]
#pprint.pprint(weather_data)