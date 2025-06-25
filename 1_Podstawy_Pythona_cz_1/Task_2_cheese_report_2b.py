
# deklaracje
cheese_name_1 = "roquefort"
cheese_price_1 = 12.50
chees_weight_1 = 2      #kg
cheese_name_2 = "stilton"
cheese_price_2 = 11.24
chees_weight_2 = 1 #kg
cheese_name_3 = "brie"
cheese_price_3 = 9.30
chees_weight_3 = 1  #kg
cheese_name_4 = "gouda"
cheese_price_4 = 8.55
chees_weight_4 = 1 #kg
cheese_name_5 = "edam"
cheese_price_5 = 11
chees_weight_5 = 1 #kg
cheese_name_6 = "parmezan"
cheese_price_6 = 16.50
chees_weight_6 = 3.5 #kg
cheese_name_7 = "mozzarella"
cheese_price_7 = 14
chees_weight_7 = 1.3 #kg / 130dag
cheese_name_8 = "czechosłowacki ser z owczego mleka"
cheese_price_8 = 122.33
chees_weight_8 = 2.2 #kg / 220dag 


# logika / kalkulacje
chees_purchase_cost_1 =chees_weight_1 * cheese_price_1
chees_purchase_cost_2 =chees_weight_2 * cheese_price_2
chees_purchase_cost_3 =chees_weight_3 * cheese_price_3
chees_purchase_cost_4 =chees_weight_4 * cheese_price_4
chees_purchase_cost_5 =chees_weight_5 * cheese_price_5
chees_purchase_cost_6 =chees_weight_6 * cheese_price_6
chees_purchase_cost_7 =chees_weight_7 * cheese_price_7
chees_purchase_cost_8 =chees_weight_8 * cheese_price_8
grand_total = chees_purchase_cost_1 + chees_purchase_cost_2 + chees_purchase_cost_3 + chees_purchase_cost_4 + chees_purchase_cost_5 +chees_purchase_cost_6 + chees_purchase_cost_7 + chees_purchase_cost_8 

# prezentacja wynikó
cheese_report = f"""Raport z zakupów:
                {cheese_name_1.ljust(35)} {chees_weight_1:>5} kg {chees_purchase_cost_1:8.2f} zł
                {cheese_name_2.ljust(35)} {chees_weight_2:>5} kg {chees_purchase_cost_2:8.2f} zł
                {cheese_name_3.ljust(35)} {chees_weight_3:>5} kg {chees_purchase_cost_3:8.2f} zł
                {cheese_name_4.ljust(35)} {chees_weight_4:>5} kg {chees_purchase_cost_4:8.2f} zł
                {cheese_name_5.ljust(35)} {chees_weight_5:>5} kg {chees_purchase_cost_5:8.2f} zł
                {cheese_name_6.ljust(35)} {chees_weight_6:>5} kg {chees_purchase_cost_6:8.2f} zł
                {cheese_name_7.ljust(35)} {chees_weight_7:>5} kg {chees_purchase_cost_7:8.2f} zł
                {cheese_name_8.ljust(35)} {chees_weight_8:>5} kg {chees_purchase_cost_8:8.2f} zł

                {"Suma:".ljust(46)} {grand_total:6.2f} zł
            
 """

print(cheese_report)
