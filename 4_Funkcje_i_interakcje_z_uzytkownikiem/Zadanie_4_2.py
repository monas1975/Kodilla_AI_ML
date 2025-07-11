# Zadanie 4_2 palindomy
# POPRAWIONE

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
    string1 = ""
    string1 = word.lower()
    string2= ""
    result = False
    
    string2=""
    for sign in string1:
        if sign.isalnum():
            string2 = string2 + sign       
    string3 = string2[::-1] 
    if string3 == string2:
         result = True
    else: 
        result = False
    return result

# palindroms
print("--------------------------------------------------------------------")
print("palindromy")
word1 = "Kobyła ma mały bok"
word2 = "kajak"
word3 = "po#to$p"

word4 = "A to kawa kota."
word5 ="Ikar bada braki."

word6 = "Ada goła im śmiało gada."
word7 =" Wół ut%ył i ma miły tuł@ów."
word8 = "Akta genera@@ła ma mała re$$negatka."

print(word1)
print(palindroms(word1))

print(word2)
print(palindroms(word2))

print(word3)
print(palindroms(word3))

print(word4)
print(palindroms(word4))

print(word5)
print(palindroms(word5))

print(word6)
print(palindroms(word6))

print(word7)
print(palindroms(word7))

print(word8)
print(palindroms(word8))


# not palindroms
print("--------------------------------------------------------------------")
print("nie sa palindromami")

word9 ="komputer"
word10 = "Nazwa palindromów pochodzi z języka"
word11 = "tom$m@ek"
word12 = "Konie@c z wystr#zeliwaniem ra**kiet"

print(word9)
print(palindroms(word9))

print(word10)
print(palindroms(word10))

print(word11)
print(palindroms(word11))

print(word12)
print(palindroms(word12))

"""
    
    
     def palindroms(word):
   
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
    
    
    
    
    """
    
   