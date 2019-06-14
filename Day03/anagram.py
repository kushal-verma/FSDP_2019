
def anagram(word1, word2):
    if len(word1) == len(word2):
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False
    else:
        return False
word1= input("Enter first word=")
word2= input("Enter second word=")
final= anagram(word1, word2)
if final == True:
    print("It's Anagram")
else:
    print("Not Anagram")