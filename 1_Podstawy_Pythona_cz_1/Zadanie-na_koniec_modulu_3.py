result_for_display =""
number = 1
while True:
    if number < 31:
        if number % 6 == 0:
            result_for_display =result_for_display + str(number) + " "
    else:
        break
    number=number+1
    pass

print(result_for_display)