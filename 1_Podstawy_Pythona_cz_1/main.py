# to sa zmiany
print("to sa zmiany na potrzeby commitu i uczenia sie githuba")
salads = {
    "owocowa": ["ananas", "truskawka", "jagody"],
    "moja_buraczana": ["buraki", "ser kozi", "rukola"],
    "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
}
print(salads["owocowa"])
salads["mięsna"]=["szynka", "kurczak", "ryż", "ogórek"]
print(salads.keys())
salads["owocowa"] = ["ananas", "truskawka", "jagody","cukier"]
print(salads["owocowa"])

salads["owocowa"].append("pomarancza")
print(salads["owocowa"])

print(salads.keys())
del salads["mamina"]
print(salads.keys())


"""
week_days = {'pon', 'wto', 'sro', 'pia', 'sob', 'nie'}
print(week_days)
week_days.update({'czw'})
print(week_days)
my_set = {1,2,4}
print(f"przed zmianami zbior to {my_set}")
my_set.update({3})
print(f"zbior po zmianach to {my_set}")
krotka = (1,2,3)
del krotka[0]
list = [100,3,6,17,4,0,-20,20]
list.sort()
print(list)
shoping_list = ["buraki", "masło", "chleb"]
shoping_list.sort
print(f"Lista po sortowani {shoping_list}")
shoping_list = ["buraki", "masło", "chleb"]
sorted_shoping_list = sorted(shoping_list)
print(f"Lista po sortowaniu {sorted_shoping_list}")
print(f"pierwotna lista {shoping_list}")



  


shoping_list = ["buraki", "masło", "chleb"]
sorted_shoping_list = sorted(shoping_list)
print(f"Lista po sortowaniu {sorted_shoping_list}")
print(f"pierwotna lista {shoping_list}")
kierunki_swiata = ["północ", "południe", "wschód", "zachód"]
print(kierunki_swiata)
del kierunki_swiata[0]
del kierunki_swiata[0]
print(kierunki_swiata)
kierunki_swiata.remove("zachód")
print(kierunki_swiata)
shoping_list = ["buraki", "masło", "chleb"]
print(shoping_list)
shoping_list[2] = "chleb bezglutenowy"
print(shoping_list)
shoping_list.append("tunczyk")
print(shoping_list)
shoping_list = shoping_list + ["śledzie"]
print(shoping_list)

del shoping_list[0]
print(shoping_list)

shoping_list.remove("masło")
print(shoping_list)
kierunki_swiata = ["polnoc", "poludnie"]
print(kierunki_swiata)
kierunki_swiata = kierunki_swiata + ["zachod"]
print(kierunki_swiata)
kierunki_swiata.append("wschod")
print(kierunki_swiata)
shopping_dict = {
    "warzywniak": ["buraki", "ziemniaki"],
    "piekarnia": ["bułka", "chleb"]
}

print(shopping_dict.keys())
print(shopping_dict.values())
#shopping_dict["skle zoologiczny"]
print(shopping_dict.get("sklep zoologiczny"))

print(shopping_dict.get("warzywniak"))


shopping_A = {"pieczywo", "masło", "ser"}
shopping_B = {"wędlina", "masło","cytryna"}
set_sum = shopping_A | shopping_B
print(set_sum)

set_sum_2 = shopping_A.union(shopping_B)
print(set_sum_2)

set_multiplication = shopping_A & shopping_B
print(set_multiplication)

set_multiplication_2 = shopping_A.intersection(shopping_B)
print(set_multiplication_2)

set_diffrence = shopping_A - shopping_B
print(set_diffrence)

set_diffrence2 = shopping_A.difference(shopping_B)
print(set_diffrence2)


days = ("pon","wto", "śro")
day_1, day_2, day_3 = days
print(day_2)
print(days[1])

shopping_list =["mielonka", "jajka", "boczek", "masło"]
print(len(shopping_list))

print(dir(shopping_list))

greetings = "cześć tomek"
print(greetings.upper())
print(greetings.capitalize())

print(dir(greetings))

shopping_dict = {
    "warzywniak": ["buraki", "ziemniaki"],
    "piekarnia": ["bulki", "chleb"]
}

print("Wchodzę do piekarni:")
print(shopping_dict["piekarnia"])



my_dictionery = dict((("klucz1", "warość1"), ("klucz2", "wartość2")))
print(my_dictionery)

my_dictionary = {
    "klucz1": "wartość1",
    "klucz2": "wartość2"
}

print(my_dictionary)

my_set = set([1,2,1])
print(my_set)
my_set = set([1,2,3])
print(type(my_set))
days = "pon", "wto", "śro", "czw", "pią","sob","nie"
print(type(days))
days = ("pon", "wto", "śro", "czw", "pią","sob","nie")
print(type(days))
days = ("pon", "wto", "śro", "czw", "pią","sob","nie")
print(type(days))
days = ("pon", "wto", "śro", "czw", "pią","sob","nie")
print(type(days))
#pierwotna lista
shopping_list =["mielonka", "jajka", "boczek"]
print(shopping_list)
# rozszerzona lista
shopping_list.append("mielonka")

print(f"Pierwszy element listy zakupów to {shopping_list[0]}")
print(f"Drugi element listy zakupów to {shopping_list[1]}")
my_list = ["Tomek", 1975, False, None, 'a', 1.74]

for element in my_list:
    print(element)

#pierwotna lista
shopping_list =["mielonak", "jajka", "boczek"]
print(shopping_list)
# rozszerzona lista
shopping_list.append("mielonka")
print(shopping_list)
tasty_cocktail = [1,"mydlo", None, "powidlo",0.1]
print(tasty_cocktail)
sentence = ["Zacznij", "kodować", "z", "Kodilla"]
for word in sentence:
    print(word)
my_list = list()
my_list = []
print(type(my_list))
print(bool(my_list))

my_list = [1,2,3,4]
for i in my_list:
    print(i)
number = 0

while True:
    if number < 100:
        if number % 3 == 0:
            print(str(number) + " jest podzielna przez 3")
    else:
        break
    number=number+1
    pass

for i in range(1,101):
    if i % 3 == 0:
        print(str(i) + " jest podzielna przez 3")

number = 0
for i in range(1,101):
    if i % 3 == 0:
        print(str(i) + " jest podzielna przez 3")


my_number = 5
if my_number < 5:
    pass
else:
    print("zmienna to 5 albo więcej!")



my_number = 5

for i in range(1,10):
    print(i)
    if i > 5:
        continue
    print("widoczne gdy i < 5")
        
for i in range(1,10):
    print(i)
    if i > 5:
        print("koniec")
        break
my_number = 3

while my_number > 0:
    print(my_number)
    my_number=my_number-1
for i in range(1,10):
    print(i)
    if i< 2:
        print("i jest mniejsze od 2 ")
    elif i<4:
        print("i jest mniejsze od 4")
    elif i<7:
        print("i jest mniejsze od 7")

print(2 > 2)
print(2<2)
print(2==2)
print(2>=2)
print(2<=2)
print(2 != 2)
raining = False

if raining:
    print("biorę parasol")
else:
    print("nie ma deszczu, nie biorę paeasola")
raining = True

if raining:
    print("biorę parasol")
print(bool(""))
print(bool(''))
print(bool(' '))
print(bool('True'))
print(bool('False'))
print(bool(0.1))
print(bool(1))
print(bool(-1))
print(bool(0))
print(bool(0.0))


my_bool = True
print(my_bool)
print(type(my_bool))
for i in range(6):
    print("*" * i)
for year in range(2020,2024):
    for month in range(1,13):
        print("Rok " + str(year))
        print("Miesiąc " + str(month) )
    break

for i in range(6):
    print("*" * i)

for year in range(2020,2024):
    for month in range(1,13):
        print("Rok " + str(year))
        print("Miesiąc " + str(month) )

word = "Tomek"
for letter in word:
    print(letter)
for i in range(20):
   print("tomek")

for i in range(20,30):
    print(i)
print("Działa !!!!")
number =44.4
print(number)
print(type(number))

print(20+20)
print(21+19)
print(5+35)

first_number = 18
second_number = 27
print(first_number+second_number)


name ="Tomasz "
surname = "Szymanski"
print(name + surname)
print(3**3)

"""
