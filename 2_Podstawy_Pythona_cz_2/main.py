#zadanie 1 
print("-------------- Zadanie 1   -------------------------------")

#deklaracja
initial_numbers_list = [1,2,3,4,5,6,7,8,9,10]

#logika
# potęgowanie (^3) wszystkich liczb w tablicy
cubed_number_list = [pow(number,3) for number in initial_numbers_list]

#prezentacja
print(cubed_number_list)

# filtrowanie liczb nie podzielnych przez 2
 
cubed_number_list_2 = [number for number in cubed_number_list if number%2 !=0]
print(cubed_number_list_2)

#zadanie 1 
print("-------------- Zadanie 2   -------------------------------")

#deklaracje
number_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
zero_list =[]
no_zero_list =[]

#logika
#lista z zerami
zero_list = number_list[1:4] + number_list[5:10] + number_list[-2:]

#n lista z wartosciami innymi, niz zero
no_zero_list = number_list[:1] + number_list[4:5] + number_list[-4:-2]

#prezentacja wynikó
print(zero_list)
print(f"ilość zer w zero_list= {len(zero_list)}")

print("------")
print(no_zero_list)
print(f"ilość licz w no_zero_list= {len(no_zero_list)}")