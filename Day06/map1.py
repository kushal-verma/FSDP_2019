import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
print (list(map(lambda names: random.choice(code_names),names)) ) 