class  BussinesCard:
    def __init__(self,first_name, second_name, company, position, email):
        self.first_name = first_name
        self.second_name = second_name
        self.company = company
        self.position = position
        self.email =email
        
    @property
    def first_second_name_lenght(self):
         return len(self.first_name + " " +  self.second_name)
        
    def __str__(self):
         return f'{self.first_name} , {self.second_name} , {self.email}'
     
    def __repr__(self):
         return f"BussinesCard(first_name= {self.first_name}, second_name={self.second_name}, company={self.company}, position={self.position}, email={self.email})"
        
    def contact(self):
        text =  f"{str(self.first_name)}  {self.second_name} , {self.company} ,{self.position}, {self.email}"
        print("Kontaktuje sie z: " + text )
        
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

print("------------------------------------------")

vb3.contact()
vb3.first_second_name_lenght
print(vb3.first_second_name_lenght)






#for item in cards:
 #   print(cards[item].first_name + " " + cards[item].second_name + " " + cards[item].email)

