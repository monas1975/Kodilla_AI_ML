# import
from faker import Faker

#definicja klas i metod

class BaseContact:
      def __init__(self,first_name, second_name, phone, email):
            self.first_name = first_name
            self.second_name = second_name
            self.phone = phone
            self.email = email
      def __str__(self):
           return f'{self.first_name} {self.second_name} {self.phone} {self.email}'
      def contact(self):
            print(f'Wybieram numner {self.phone} i dzwonię do {self.first_name} {self.second_name}')
      
class BusinessContact(BaseContact):
      def __init__(self, position, company_name, business_phone, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.position = position
           self.company_name = company_name
           self.business_phone = business_phone
      def __str__(self):
           return f'{self.first_name} {self.second_name} {self.phone} {self.email} {self.position} {self.company_name} {self.business_phone}'
      def contact(self):
            print(f'Wybieram numner {self.business_phone} i dzwonię do {self.first_name} {self.second_name}')





#Funkcja tworząca wizytówke
def create_card(type_of_card, amount):
    """
    Create a list of objext ; base_contact object or business_contacts
    Args: 
        type_of_cards as string; base or business contacts
        amount as int - amout of contact created
    Return: list of object (base_contact or business contacts)
    
    """
    base_contact_list = []
    business_contact_list = []
    if type_of_card == "BaseContact":
     for i in range(0,amount):
        fake_person1 =  Faker("PL")
        result = BaseContact(first_name = fake_person1.first_name(), second_name=fake_person1.last_name(),
                              phone= fake_person1.phone_number(), email = fake_person1.email() )
        base_contact_list.append(result)
     return base_contact_list
    if type_of_card == "BusinessContact":
      for i in range(0,amount):
        fake_person1 =  Faker("PL")
        fake_person2 = Faker("PL")
        result = BusinessContact(first_name = fake_person1.first_name(), second_name=fake_person1.last_name(), 
                                 phone= fake_person1.phone_number(), email = fake_person1.email(),
                                 position =  fake_person1.job() ,company_name= fake_person1.company,business_phone=  fake_person2.phone_number()
                                   )
        business_contact_list.append(result)
    return business_contact_list
         
     

# Prezentacja wyników z użycie funkcji contact()

# base contact
print("Base Contact")
base_cards = create_card("BaseContact", 10)
for i in range(0, len(base_cards)):
    base_cards[i].contact()
print("-----------------------------------------------------------------")
# business contacts
print("Business Contact")
business_cards = create_card("BusinessContact", 10)
for i in range(0, len(business_cards)):
    business_cards[i].contact()

print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
#Prezentacja stworzonych obiektów
print("Prezentacja stworzonych obiektów")
print("base contact")
for i in range(0, len(base_cards)):
    print(base_cards[i])

print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")

for i in range(0, len(business_cards)):
    print(business_cards[i])
