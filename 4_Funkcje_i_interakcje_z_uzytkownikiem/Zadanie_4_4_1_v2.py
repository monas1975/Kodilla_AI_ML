import sys
import logging

# deklaracje zmiennych 
math_operation = ""
numbers =[]
numbers_for_cal =[]
a=0
b=0

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename= "logfile.log")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def is_float(s):
    """_summary_
     funkction checking if string represent float value
    Args:
        strings

    Returns:
        _boolean value True or False
    """  
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    """
    funkction checking if string represent integer value
    Args:
        string

    Returns:
        boelan value True or False
    """
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def math_cal_adding(numbers):
    """
     Function add values from list deliverd as argument
    Args:
        numbers - list of values (float)
    Returns: result as float
    """
    
    text=""
    result=0
    
    for i in range(0,len(numbers)):
            result = result + float(numbers[i])
            text = text +  " i " + str(numbers[i])
    text = "Dodawanie: "  + text
    logging.info(text)
    return result

def math_cal_sub(numbers):
    """
     Function substract values from list deliverd as argument
    Args:
        numbers - list of values (float)
    Returns: result as float
    """
    text=str(numbers[0])
    result=float(numbers[0])
    for i in range(1,len(numbers)):
            result = result - float(numbers[i])
            text = text +  " i " + str(numbers[i])
    text = "Odejmowanie: "  + text
    logging.info(text)
    return result

def math_cal_multi(numbers):
    """
     Function multiplicate values from list deliverd as argument
    Args:
        numbers - list of values (float)
    Returns: result as float
    """
    
    text=""
    result=1
    
    for i in range(0,len(numbers)):
            result = result * float(numbers[i])
            text = text +  " i " + str(numbers[i])
    text = "Mnoenie: "  + text
    logging.info(text)
    return result

def math_cal_div(numbers):
    """
     Function divide values from list deliverd as argument
    Args:
        numbers - list of values (float)
    """
    
    text=str(numbers[0])
    result=float(numbers[0])
    
    for i in range(1,len(numbers)):
        if numbers[i] !=0:
            result = result / float(numbers[i])
            text = text +  " przez " + str(numbers[i])
        else:
            print("dzielenie przez 0 jest niedozwolone, wychodze z programu")
            exit(1)
    text = "Dzielenie: "  + text
    logging.info(text)
    return result

def math_operation_choose():
    """
    Fnction collect imput form consol to choose Math operation, that will be used.
    Args: None

    Returns:
        math_operation as string
    """
    print("Wybr operacji matematycznej")
    print("Aby wyj z programu wprowadz litere lub liczbe >= 5")
    math_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:    ")
    if math_operation !='1' and math_operation !='2' and math_operation !='3' and math_operation != '4':
        print("wychodz z programu, nie wybrano adnej operacji matematycznej ")
        exit(0)
      
    return math_operation


def entering_numbers_in_loop():
    print("Aby wyjsc z trybu wprowadzania liczb, wcisnij dowolna litere")
    while True:
            c = input("Podaj liczbę: ")
            if is_float(c) or is_int(c):
                numbers.append(float(c))
            else:
                print(" nie została wprowadzona liczba, koncze wprowadzanie liczb")
                break
    return numbers

def entering_two_numbers():
    a = input("Podaj 1sza liczbe:  ")
    if is_float(a) or is_int(a):
            numbers.append(float(a))          
    else: 
        exit(1)
    b = float((input("Podaj 2ga liczbe:   ")))
    if is_float(b) or is_int(b):
            numbers.append(float(b))
    else: 
        print(" nie została wprowadzona liczba, wychodzę  z programu")
        exit(1)
    return numbers

if __name__ == "__main__":
    math_operation = math_operation_choose()
    
if math_operation =='2':
    print("wynik to:   " +str(math_cal_sub(entering_two_numbers())))
elif math_operation == '4':
    print("wynik to:  " + str(math_cal_div(entering_two_numbers())) )
elif math_operation =='1':
    print("Wynik to:   " + str(math_cal_adding(entering_numbers_in_loop())))
else:
    print("Wynik to:   " + str(math_cal_multi(entering_numbers_in_loop())))

    
   






