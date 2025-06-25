# zadanie 1
#POPRAWIONE
print("-------- Zadanie 1    -----------------------")
my_list = ["John", "Michael", "Terry", "Eric", "Graham"]
print(type(my_list))  #chcek if list


name_dictionary = {} #empty dictionary declaration

for i in range(0,len(my_list)):
   name_dictionary[my_list[i]] = len(my_list[i])
 

print(type(name_dictionary)) #chcek if dictionary
print(name_dictionary.keys()) #check keys
print(name_dictionary.values()) #check values
print(name_dictionary) #show dictionary


##  Zadanie 2
#Poprawione - zmieniony algorytm
print()
print("-------- Zadanie 2    -----------------------")

#declaration
initial_number_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
prime_numbers=[]  # empty prime number list initialization
#prime_number =0


#logic

#definuj funkcje, ktora sprawdza czy dana liczba jest liczbą pierwszą czy nie.
#jesli jest liczbą pierwszą funkcja zwraca True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for number in initial_number_list:
    if is_prime(number):
        prime_numbers.append(number)
        

 # result presentation             
print(prime_numbers)

##  Zadanie 3

#POPRAWIONE
#noe wiem czy dobrze zrozumiaem uwagi do mojego poprzedniego rozwizania.

print()
print("-------- Zadanie 3    -----------------------")



#declaration

weekdays_list_for_task = ['pon','śro','pią','sob']  # tablice wejsciowa

full_list_of_weekddays = ['pon','wto','śro','czw', 'pią','sob', 'niedz']  #tablica referencyjan

weekdays_list_for_task.insert(1,full_list_of_weekddays[1])
weekdays_list_for_task.insert(3,full_list_of_weekddays[3])
weekdays_list_for_task.insert(6,full_list_of_weekddays[6])



print(weekdays_list_for_task)
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





