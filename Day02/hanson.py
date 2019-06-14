# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:12:59 2019

@author: kushal
"""


hands_list =list(range(21))
print(type(hands_list))
print(hands_list)
print("even numbers: ", hands_list[0::2])
print("odd numbers: ",hands_list[1::2])



def leap():
   if(year%4==0 and year%100!=0 or year%400==0):
    return True
   else:
    return False
year=int(input("enter year to be checked"))
print(year)
leap()




def day_in_month(month):
  if month=="April" or "June" or "september" or "november":
        return 30
  if month=="January" or "March" or  "May" or "July" or "August" or "October" or "December":
        return 31
  if month=="February":
      year=int(input("enter year"))
      if(year%4==0 or year%400==0 and year%100!=0):
          return 29
      else: 
          return 28
                 
        
        















    