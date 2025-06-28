
def palindroms(word):
    """
    Check if the string passed as parametr is a palindrom.
    Arguments:
        word
    Return:
    True if a word is a palindrom.
    False if not a palindrom.    
    """
    string1 = word.lower()
    string2 = ''
    
    for i in range(len(string1)-1,-1,-1):
        string2 += string1[i] 
    if string1 == string2:
        return True
    else: return False

word ="Potop"
print("Cze slowo " + word + " jest palindromem True / False : " + str(palindroms(word)))

#string3 = "Andrzej"
#print(string3[0])
#print(string3[len(string3)-1])

#('tomek' == 'anka')
#print('tomek' == 'tomek')