import csv
from csv import DictReader
from sqlalchemy import Table, Column, Integer, String,Float, MetaData,insert, update, select
from sqlalchemy import create_engine, text
from Zadanie_6_3_1 import engine, clean_station
from sqlalchemy.orm import Session


def insert_dic_to_table(dic):
    """
    insert data from list of dictionaries to clean station table
    """
    ins = clean_station.insert()
    #ins = clean_station.insert().values(station='1dft', date='13-01-2001')
    conn = engine.connect()
    #result = conn.execute(ins,)
    result = conn.execute(ins,dic)

def update_table(dic):
    """
    update data rom list of dictionaries to clean station table
    """
    for item in dic:
     stmt = clean_station.update().where(clean_station.c.station == item.get('station'))
     conn = engine.connect()
     result = conn.execute(stmt,item)

def csv_to_list_of_dic(file):
    """
     read csv file into list of dictioneries
    """
    with open(file, 'r') as f:  
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
    return list_of_dict




if __name__== '__main__':

    file_1 = 'D:\\Kodilla_AI_ML\\6_Bazy_danych\\Zadanie_6_3_1\\clean_measure.csv'
    file_2 = 'D:\\Kodilla_AI_ML\\6_Bazy_danych\\Zadanie_6_3_1\\clean_stations.csv'

    # wprowadzanie danych
    print("wprowadzanie danych")
    dic1 = csv_to_list_of_dic(file_1)
   # insert_dic_to_table(dic1)

     #  update rekordów
    print("update danych")
    dic2 = csv_to_list_of_dic(file_2)
   # update_table(dic2)

    #select
    # conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print("_______________        SELECT 1  ________________________________")
print("         SELECT * FROM stations LIMIT 5                         ")

metadata = MetaData()
clean_station = Table("clean_station", metadata, autoload_with=engine)

stmt = select(clean_station).limit(5)  # lub zmienna limit_value

with engine.connect() as conn:
    results = conn.execute(stmt).fetchall()

for row in results:
   print(row)

# # conn.execute("SELECT * FROM clean_stations WHERE elevation > 300).fetchall()
print("_______________        SELECT 2  ________________________________")
print("         SELECT * FROM clean_stations WHERE elevation > 300 LIMIT 5                         ")


stmt = select(clean_station).where(clean_station.c.elevation > 300).limit(5)  # lub zmienna limit_value

with engine.connect() as conn:
    results = conn.execute(stmt).fetchall()

for row in results:
   print(row)