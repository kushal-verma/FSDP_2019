
from collections import OrderedDict
string= input("Enter string=")
dict1= OrderedDict()
dict1["Digits"]= 0
dict1["Letters"]= 0
for character in string:
    if character.isalpha():
        dict1["Letters"]=dict1["Letters"] + 1
    elif character.isdigit():
        dict1["Digits"]=dict1["Digits"] + 1
for key, value in dict1.items():
    print(key, value)
