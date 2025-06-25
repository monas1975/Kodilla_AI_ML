
# zadanie 1
print("-------- Zadanie 1    -----------------------")
my_list = ["John", "Michael", "Terry", "Eric", "Graham"]
print(type(my_list))  #chcek if list


name_dictionary = {} #empty dictionary declaration

for i in range(0,len(my_list)):
   name_dictionary[my_list[i]] = [len(my_list[i])]
 

print(type(name_dictionary)) #chcek if dictionary
print(name_dictionary.keys()) #check keys
print(name_dictionary.values()) #check values
print(name_dictionary) #show dictionary

##  Zadanie 2
print()
print("-------- Zadanie 2    -----------------------")

#declaration
initial_number_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
prime_numbers=[]  # empty prime number list initialization

#logic
for i in range(0,len(initial_number_list)):
   number_tested = initial_number_list[i]
   #print(f"number_tested = {number_tested}" )
   if number_tested == 1:
      False
   elif number_tested == 2:
    prime_numbers.append(number_tested)
   else:
    for n in range(2,number_tested):
      if (number_tested % n ) == 0:
        break
      elif ((number_tested !=3) and (number_tested % 3 == 0))  or ((number_tested !=7) and (number_tested % 7)==0):
        False
      else:
        prime_numbers.append(number_tested)
        break
 # result presentation             
print(prime_numbers)

##  Zadanie 2
print()
print("-------- Zadanie 3    -----------------------")

#full_weekdays_list = ["pom"]

#declaration

weekdays_list_for_task = ['pon','śro','pią','sob']  # tablice wejsciowa

full_list_of_weekddays = ['pon','wto','śro','czw', 'pią','sob', 'niedz']  #tablica referencyjan

list_of_diffrent_elements =[]
temp_dic={}

# prezentacja listy przed aktualizacją
print("lista wejsciowa przed aktualizacja:")
print("")
print(weekdays_list_for_task)
print("")

# sprawdzam które dni nie występują w tablicy weekdays_list_for_tsk

      
list_of_diffrent_elements = [item for item in full_list_of_weekddays if item not in weekdays_list_for_task]

# sprawdzam pod którym indexem w liście referencyjnej występują rożniące się obiekty i tworze słownik element : klucz


for element in list_of_diffrent_elements:
  temp_dic.update({element : full_list_of_weekddays.index(element)})

# aktualizuje listę wejsciową (weekdays_list_for_task)


for key in temp_dic:
  weekdays_list_for_task.insert(temp_dic[key], key)
  
# prezentacja wyników
print("list wejsciowa po aktualizacji:")
print("")
print(weekdays_list_for_task)

print("")
print("")
print("-----------------   Zadanie 4 ----------------------------------------")
"""
Zadanie 4
Oto sekwencja kroków do zrobienia herbaty.

włącz czajnik
znajdź opakowanie herbaty
zalej herbatę
nalej wody do czajnika
wyjmij kubek
włóż herbatę do kubka

"""

tee_preparation_list = ["włącz czajnik", "znajdź opakowanie herbaty","zalej herbatę","nalej wody do czajnika","wyjmij kubek","włóż herbatę do kubka"]
print("list niezgodna z sekwencja parzenia herbaty:")
print(tee_preparation_list)
temp_list =[]


# kopiuje elementy do tablicy tymczasowej

temp_list = tee_preparation_list.copy()


# usuwam elementy z listy wejsciowej
tee_preparation_list.clear()

# kopiuje elementy z listy tymczasowej, zgodnie z sekwencja parzenia herbaty

tee_preparation_list.insert(0,temp_list[1])
tee_preparation_list.insert(1,temp_list[3])
tee_preparation_list.insert(2,temp_list[0])
tee_preparation_list.insert(3,temp_list[4])
tee_preparation_list.insert(4,temp_list[5])
tee_preparation_list.insert(5,temp_list[2])


print("") 
print(" lista posortowana zgodnie z sekwencja parzenia herbaty:")
print("")
print(tee_preparation_list)





