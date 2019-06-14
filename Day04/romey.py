# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:41:21 2019

@author: kushal
"""

with open('romey.txt', mode='wt') as file :
          list_of_lines= file.readlines()
          word_dict={}

          for line in list_of_lines:
              words_list= line.split()
              if word in words_list :
                word_dict[word]=1
              else:
                word_dict[word]=1
for key, value in word_dict.items():
          print[key, value]