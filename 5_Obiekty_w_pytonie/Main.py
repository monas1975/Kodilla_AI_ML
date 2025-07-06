class Car:
    def __init__(self,make, model_name,top_speed,color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color
       #Variables
       self._current_speed = 0
   # def __str__(self):
    #    return f'{self.color} {self.make} {self.model_name}'
    @property
    def current_speed(self):
         return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
         self._current_speed = value
        else:
           raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")
    
    def __repr__(self):
        return f"Car(make= {self.make}, model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
    
    
    def __eq__(self, other):
        return (
            self.make == other.make and
            self.model_name == other.model_name and
             self.top_speed == other.top_speed and
              self.color == other.color
              )
    
    def __eq__(self, other):
     return all(
        (
            self.make == other.make,
            self.model_name == other.model_name,
            self.top_speed == other.top_speed,
            self.color == other.color
        )
    )
     
     
     
    def __gt__(self, other):
        return self.top_speed > other.top_speed
   
    def accelerate(self, step=10):
        self.current_speed +=10
    
    def decelerate(self, step=10):
        self.current_speed -=10
   
    
mustang  = Car(make = "Ford", model_name="Mustang", color = "Yellow", top_speed = 250) 
car =  Car(make = "Ford", model_name="Mustang", color = "Red", top_speed = 250)     
car2 =  Car(make = "Ford", model_name="Mustang", color = "Blue", top_speed = 250)   
car3 =  Car(make = "Ford", model_name="Mustang", color = "Blue", top_speed = 250)    
car4 =  Car(make = "Ford", model_name="Focus", color = "Blue", top_speed = 200)  

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]

by_speed = sorted(cars, key=lambda car: car.top_speed)
by_make = sorted(cars, key=lambda car: car.make)

print(mustang)
print(mustang.make)
print(mustang)
print(car)
print(car2 ==car3)
print(mustang == car3)
print(car3 > car4)
print("------------------------------------")

print(by_make)
print(by_speed)

print("------------------------------------")
print(mustang)
print(mustang.current_speed)
mustang.accelerate()
mustang.accelerate()
mustang.accelerate()
print(mustang.current_speed)
mustang.decelerate()
print(mustang.current_speed)

print("------------------------------------")
print(car2)
print(car2.current_speed)
#car2.current_speed()
car2.current_speed =100
print(car2.current_speed)
car2.current_speed =400
print(car2.current_speed)
"""


class  BussinesCard:
    def __init__(self,first_name, second_name, company, position, email):
        self.first_name = first_name
        self.second_name = second_name
        self.company = company
        self.position = position
        self.email =email
        
    def __str__(self):
         return f'{self.first_name} , {self.second_name} , {self.email}'
     
    def __repr__(self):
         return f"BussinesCard(first_name= {self.first_name}, second_name={self.second_name}, company={self.company}, position={self.position}, email={self.email})"
        
vb1 = BussinesCard(first_name = "Tomasz", second_name= "Szymanski", company="ABC", position="inzynier", email = "t_szymanski@abc.com")
vb2 = BussinesCard(first_name = "Marek", second_name= "Markowski", company="DEF", position="kierownik", email = "Marek.Markiewicz@def.com")
vb3 = BussinesCard(first_name = "Piotr", second_name= "Piotrowski", company="GHI", position="dyrekto", email = "p_piotrowski@ghi.com")
vb4 = BussinesCard(first_name = "Anna", second_name= "Szymansk", company="argenta", position="kierownik sprzedazy", email = "a_szymanska@argent.pl")
vb5 = BussinesCard(first_name = "Ewa", second_name= "Wachowiak", company="JKL", position="sprzedawca", email = "ewa.wachowiak@JKL.com")

print(dir(BussinesCard))

cards = [vb1,vb2,vb3,vb4,vb5]

for i in range(0, len(cards)):
    print(cards[i].first_name + " " + cards[i].second_name + " " + cards[i].email)

print("------------------------------------------")
print(vb1)
print(vb5)

#by_speed = sorted(cars, key=lambda car: car.top_speed)
print("------------------------------------------")
by_first_name = sorted(cards, key=lambda card: card.first_name)
print(by_first_name)
print("------------------------------------------")
by_second_name = sorted(cards, key=lambda card: card.second_name)
print(by_second_name)
print("------------------------------------------")
by_email = sorted(cards, key=lambda card: card.email )










for item in cards:
    print(cards[item].first_name + " " + cards[item].second_name + " " + cards[item].email)


class Car:
    def __init__(self,make, model_name,top_speed,color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self_color = color
       
mustang  = Car(make = "Ford", model_name="Mustang", color = "Yellow", top_speed = 250)       

print(mustang)
print(mustang.make)


my_car = Car()

print(type(my_car))
    
    class Car:
    pass
    
    
    
    
   car = Car(
    make="Ford",
    model_name = "Mustang",
    top_speed  = 250,
    color = "Red"
)

car.curent_speed = 100

def set_current_speed(self, value):
    if value <= self.top_speed:
       self.current_speed - value
    else:
        raise ValueError(f"Value {value} exceed top speed of {self.top_speed}") 


print(car.top_speed)
 
    
    
"""