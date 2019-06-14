
string= input("Enter string=")
character_freq={}
for alpha in string:
    character_freq[alpha]=character_freq.get(alpha,0) + 1
print(character_freq)
from collections import Counter
print(dict(Counter(string)))
