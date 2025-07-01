



def palindroms(word):
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
    
    def palindrom(word):
    string1 =word.lower()
    text1 = [for sign in string1 if sign.isalnum]
    
    
"""
