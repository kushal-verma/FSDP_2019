

def translate(string):
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    final_list = []

    for element in string:
        if element in consonants: 
            final_list.append(element+"o"+element)
        else:
            final_list.append(element)

    return "".join(final_list)
string = input("Enter a string >")
print (string)
translate(string)