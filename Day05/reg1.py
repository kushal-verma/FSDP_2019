
import re
number_list= list()

while True:
    number= input("Enter number=")
    if not number:
        break
    number_list.append(number)

result_list=[]
for number in number_list:
     if re.match(r'^[+-]?\d*\.\d*$', number):
         result_list.append(True)
     else:
         result_list.append(False)

print(result_list)