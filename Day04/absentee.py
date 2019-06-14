# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:12:56 2019

@author: kushal
"""
count=0  
with open('absentee.txt', mode='wt') as file :
    while(count<15):
       name=input("enter name")
       count +=1
       file.write(name+ '\n')
       if not name :
          break
if name =="":
    print("you entered non value!")
else:
    with open('absentee.txt', mode='rt') as file :
          for line in file:
              name = file.readlines()
              print(name)
            
        