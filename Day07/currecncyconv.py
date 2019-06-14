# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:09:52 2019

@author: kushal
"""

import requests
url="http://data.fixer.io/api/latest?access_key=48d774bd3ef997c5588a5ba70b0d35ba&format=1"
current_USD_in_INR = requests.get(url).json()['EUR_INR']
print("Equivalent INR: ",round( float(input("Enter USD: "))*current_USD_in_INR, 2))