
item_dict={}
dict1 = {}
while(True):
 user_input= input("Enter items=")   
 if not user_input:
     break
 input_item=user_input.split()
 item_name=' '.join(input_item[:-1])
 item_price=input_item[-1]
 
 if item_name not in item_dict:
     item_dict[item_name]=item_price
 else:
     item_dict[item_name]=int(item_dict[item_name])+ int(item_price)
print(list(item_dict.items()))
     