# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:21:34 2019

@author: kushal
"""

with open('words.txt',mode='rt') as file:
       file_contents = file.readlines()
       print(file_contents[-1])