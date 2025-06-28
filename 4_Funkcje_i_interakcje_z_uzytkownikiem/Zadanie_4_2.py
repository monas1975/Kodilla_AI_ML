# Zadanie 4_2 palindomy

# definicja funkcji
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

word ="kajak"
print("Cze slowo " + word + " jest palindromem True / False : " + str(palindroms(word)))

word ="drzewo"
print("Cze slowo " + word + " jest palindromem True / False : " + str(palindroms(word)))

