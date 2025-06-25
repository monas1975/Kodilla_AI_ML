cheeseName1 = "roquefort"
cheesePrice1 = 12.50
cheesWeight1 = 2      #kg
cheeseName2 = "stilton"
cheesePrice2 = 11.24
cheesWeight2 = 1 #kg
cheeseName3 = "brie"
cheesePrice3 = 9.30
cheesWeight3 = 1  #kg
cheeseName4 = "gouda"
cheesePrice4 = 8.55
cheesWeight4 = 1 #kg
cheeseName5 = "edam"
cheesePrice5 = 11
cheesWeight5 = 1 #kg
cheeseName6 = "parmezan"
cheesePrice6 = 16.50
cheesWeight6 = 3.5 #kg
cheeseName7 = "mozzarella"
cheesePrice7 = 14
cheesWeight7 = 1.3 #kg / 130dag
cheeseName8 = "czechosłowacki ser z owczego mleka"
cheesePrice8 = 122.33
cheesWeight8 = 2.2 #kg / 220dag 

cheeseReport = f"""Raport z zakupów: 
                  {cheeseName1}, {cheesWeight1} kg,  {cheesWeight1 * cheesePrice1:.2f} zł,
                  {cheeseName2}, {cheesWeight2} kg,  {round(cheesWeight2 * cheesePrice2,2)} zł,
                  {cheeseName3}, {cheesWeight3} kg,  {cheesWeight3 * cheesePrice3:.2f} zł,
                  {cheeseName4}, {cheesWeight4} kg,  {round(cheesWeight4 * cheesePrice4,2)} zł,
                  {cheeseName5}, {cheesWeight5} kg,  {cheesWeight5 * cheesePrice5:.2f} zł,
                  {cheeseName6}, {cheesWeight6} kg,  {round(cheesWeight6 * cheesePrice6,2)} zł,
                  {cheeseName7}, {cheesWeight7} kg,  {cheesWeight7 * cheesePrice7:.2f} zł,
                  {cheeseName8}, {cheesWeight8} kg,  {round(cheesWeight8 * cheesePrice8,2)} zł,
                  ----------------------------------------------------------------------------
                  Suma zł: {round(cheesWeight1 * cheesePrice1 + 
                                  cheesWeight2 * cheesePrice2 +
                                  cheesWeight3 * cheesePrice3 +
                                  cheesWeight4 * cheesePrice4 +
                                  cheesWeight5 * cheesePrice5 +
                                  cheesWeight6 * cheesePrice6 +
                                  cheesWeight7 * cheesePrice7 +
                                  cheesWeight8 * cheesePrice8
                                  ,2)}
                 """ 
print(cheeseReport)

## drugi sposob
cheesPurchaseCost1 =round(cheesWeight1 * cheesePrice1,2)
cheesPurchaseCost2 =round(cheesWeight2 * cheesePrice2,2)
cheesPurchaseCost3 =round(cheesWeight3 * cheesePrice3,2)
cheesPurchaseCost4 =round(cheesWeight4 * cheesePrice4,2)
cheesPurchaseCost5 =round(cheesWeight5 * cheesePrice5,2)
cheesPurchaseCost6 =round(cheesWeight6 * cheesePrice6,2)
cheesPurchaseCost7 =round(cheesWeight7 * cheesePrice7,2)
cheesPurchaseCost8 =round(cheesWeight8 * cheesePrice8,2)
grandTotal = cheesPurchaseCost1 + cheesPurchaseCost2 + cheesPurchaseCost3 + cheesPurchaseCost4 + cheesPurchaseCost5 +cheesPurchaseCost6 + cheesPurchaseCost7 + cheesPurchaseCost8 

print()
print("----------------drugi sposob ----------------------------------------------------------------------") 
cheeseReport2 = f"""Raport z zakupów: 
                  {cheeseName1}, {cheesWeight1} kg,  {cheesPurchaseCost1:.2f} zł,
                  {cheeseName2}, {cheesWeight2} kg,  {cheesPurchaseCost2:.2f} zł,
                  {cheeseName3}, {cheesWeight3} kg,  {cheesPurchaseCost3:.2f} zł,
                  {cheeseName4}, {cheesWeight4} kg,  {cheesPurchaseCost4:.2f} zł,
                  {cheeseName5}, {cheesWeight5} kg,  {cheesPurchaseCost5:.2f} zł,
                  {cheeseName6}, {cheesWeight6} kg,  {cheesPurchaseCost6:.2f} zł,
                  {cheeseName7}, {cheesWeight7} kg,  {cheesPurchaseCost7:.2f} zł,
                  {cheeseName8}, {cheesWeight8} kg,  {cheesPurchaseCost8:.2f} zł,
                  ----------------------------------------------------------------------------
                  Suma zł: {grandTotal:.2f} """   

print(cheeseReport2)           