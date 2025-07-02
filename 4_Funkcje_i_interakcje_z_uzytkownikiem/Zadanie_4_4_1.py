import sys
import logging

numbers =[]
a=0
b=0

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename= "logfile.log")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def math_calculation(operation_type, numbers):
    #print("jestem w fumlcji 1")
    #print(type(math_operation))
    #print(operation_type)
    text=""
    calculation_type= operation_type
    result=0
    if operation_type == '1':
        calculation_type ="Dodaję "
        for i in range(0,len(numbers)):
            result = result + float(numbers[i])
            text = text +  " i " + str(numbers[i])
        text = " " + calculation_type + ":  " + text
        logging.info(text)
        print("Wynik to:  " + str(result))
            
    elif operation_type == '2':
        #print("jestem w funkcji")
        calculation_type = "Odejmuje "
        #print(type(math_operation))
        text=""
        calculation_type= operation_type
        result=0
        if operation_type == '2':
          calculation_type ="Odejmuje "
          result = float(numbers[0]) - float(numbers[1])
          text = str(float(numbers[0])) + " i " +  str(float(numbers[1]))
        text = " " + calculation_type + ":  " + text
        logging.info(text)
        print("Wynik to:  " + str(result))
        
    elif operation_type == '3':
        calculation_type = "Mnożę"
        result = 1
        
        for i in range(0,len(numbers)):
            result = result * float(numbers[i])
            text = text +  " i " + str(numbers[i])
        text = " " + calculation_type + ":  " + text
        logging.info(text)
        print("Wynik to:  " + str(result))
    else: 
        calculation_type = "Dzielę"
        result = float(numbers[0]) / float(numbers[1])
        text = str(float(numbers[0])) + " przez " +  str(float(numbers[1]))
        text = " " + calculation_type + ":  " + text
        logging.info(text)
        print("Wynik to:  " + str(result))
    
        





if __name__ == "__main__":
    print("Aby wyjsc z trybu wprowadzanie liczb, wcisnij dowolna litere")
    math_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:    ")
    if math_operation == '2' or math_operation == '4':  
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
    elif math_operation == '1' or math_operation == '3': 
        while True:
            c = input("Podaj liczbę: ")
            

            if is_float(c) or is_int(c):
                numbers.append(float(c))
            else:
                print(" nie została wprowadzona liczba, koncze wprowadzanie liczb")
                break
    else: 
        logging.info("nie ma takiego działania")
        exit(1)

print(math_operation)
print("-------------------")
math_calculation(math_operation, numbers)