# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:24:05 2019

@author: kushal
"""

import json
import requests

Host = "https://enpru3lpltm2m.x.pipedream.net"

data = {"firstname":"kushal","language":"English"}
headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("https://enpru3lpltm2m.x.pipedream.net/get?firstname=Dev&language=English")
    return response

print (get_method().text)
