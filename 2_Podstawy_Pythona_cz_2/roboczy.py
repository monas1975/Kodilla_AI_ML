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