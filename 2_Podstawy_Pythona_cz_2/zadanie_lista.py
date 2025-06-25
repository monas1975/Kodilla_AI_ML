weekdays_list_for_task = ['pon','śro','pią','sob']
#print(len(weekdays_list_for_task))

full_list_of_weekddays = ['pon','wto','śro','czw', 'pią','sob', 'niedz']

for i in range(0,len(weekdays_list_for_task)):
    if full_list_of_weekddays[i] != weekdays_list_for_task[i]:
        weekdays_list_for_task.insert(i,full_list_of_weekddays[i])
        print("len=" + str(len(weekdays_list_for_task)))
    else:
        False
        
print(weekdays_list_for_task)
        