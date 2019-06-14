name=input("Enter a name>")
index = name.find(' ')
print(name[index:] + " " + name[:index] )