from  faker import Faker

fakePersons =[]

for i in range(0,10):
    fakePersons.append(Faker('PL'))

for i in range(0, len(fakePersons)):
        # print("----------" + str(i) + "--------------------------------------------")
        imię = fakePersons[i].first_name()
        nazwisko = fakePersons[i].last_name()
        adres = fakePersons[i].address()
        email = fakePersons[i].email()
        telefon = fakePersons[i].phone_number()
        company = fakePersons[i].company()
        position = fakePersons[i].job()
        print(f"Imię: {imię}")
        print(f"Nazwisko: {nazwisko}")
        print(f"Adres: {adres}")
        print(f"Email: {email}")
        print(f"Telefon: {telefon}")
        print(f"Firma {company}")
        print(f"Stanowisko: {position}")
       #print("--------------------------------------------------------------------")


