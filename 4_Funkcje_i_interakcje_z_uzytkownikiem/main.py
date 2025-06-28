
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
"""
shopping_items = [
    "jaja",
    "bulka",
    "ser_feta",
    "maslo",
    "pomidor",
    "chusteczki",
    "papier toaletowyh"
    
]



def shopping(items, *,payment='card', shop='local'):
    pass
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart +=item + '\n'
    shopping_cart = shopping_cart + '\n' + payment + '\n' + shop
    return shopping_cart



basket1 = shopping(shopping_items, 'cash')
print(basket1)



shopping_items = [
    "jaja",
    "bulka",
    "ser_feta",
    "maslo",
    "pomidor",
    "chusteczki",
    "papier toaletowyh"
    
]



def shopping(items, payment='card', shop='local'):
    pass
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart +=item + '\n'
    shopping_cart = shopping_cart + '\n' + payment + '\n' + shop
    return shopping_cart



basket1 = shopping(shopping_items)
print(basket1)

basket2 = shopping(shopping_items, 'card','supermarket')
print(basket2)

basket3 = shopping(shopping_items, 'card')
print(basket3)

basket4 = shopping(shopping_items, shop='hipermarkt"')
print(basket4)


def customized_hello(first_name,last_name, gender_prefix='Mr'):
    print(f"Hello {gender_prefix} {first_name} {last_name} !")
    
customized_hello("Tomasz", "Szymanski")

customized_hello("Anna", "Szymanska", "Ms")

def customized_hello(first_name,last_name):
    print("Hello Mr %s %s" % (first_name, last_name))
    
customized_hello("Tomasz", "Szymanski")

def add(a,b):
     print(a+b)

add(10,5)

def day_times():
    return "morning", "afternoon","evening", "night"

times = day_times()
print(times)
print(type(times))

first, second, third, fourth = day_times()
print("trzeci element to %s" %third)

def no_result_function():
    print("aaaa")
    print("bbbb")

no_result_function()

print(type(no_result_function()))

def shopping():
    shopping_items = [
       "jajka",
       "bulka",
       "ser feta",
       "maslo",
       "pomidor" 
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

print(shopping())
a=1
  
def scope_demo():
    a=2
    print(a) 

scope_demo()
print(a)

def add_two_numbers():
    print("5 + 6 = "  + str(5+6))
add_two_numbers()

def demo_function():
print("I am inside of a function")
    
demo_function() 
    
    
"""