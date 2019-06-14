s = input("Enter numbers>").split(" ")
for i in s:
    flag1=False
    if i[::-1]==i:
        flag1=True
        break
    else:
        flag1=False
flag2=True
for i in s:
  p=int(i)
  if(p < 0):
    flag2=False


if(flag1==True and flag2==True):
 print("True")
else:
 print("False")
    