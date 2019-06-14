# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:32:35 2019

@author: kushal
"""

file_name= input("please enter file name: ")

def word_count(file_name):
   with open(file_name, mode='rt') as file:
       list_of_lines = file_readlines()
       lines_count = len(list_of_lines)
       
       word_dict = {}
       characters_count= 0
       
       for word in words_list:
           
           if word not in list(word_dict_keys()):
               word_dict[word] = 1
           else:
               word-dict[word] == 1
   unique_words_count = len(list(word_dict_keys()))
    
   words_count = 0
   for value in word_dict.values():
       words_count += value
   return characters_count, words_count, lines_count, unique_words_count
characters, words, lines, unique_words = word_count(file_name)
print("Total characters:", characters)
print("Total words:", words)
print("Total lines:",lines)
print("Total unique words:", unique_words)
       
       
       
        
          
               
               