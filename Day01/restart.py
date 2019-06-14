name = 'restart'
str1 = name.replace('r','$')
str1 = name.replace('$','r',1)

name1 = name[1:]
str1 = name.replace('r','$')
print(name[0]+str1)   