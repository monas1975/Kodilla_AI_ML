import csv
from csv import DictReader
from sqlalchemy import Table, Column, Integer, String,Float, MetaData,insert
from sqlalchemy import create_engine
from sqlalchemy.dialects import sqlite
from sqlalchemy import BigInteger

#BIGINT = BIGINT().with_variant(sqlite.INTEGER, "sqlite")
engine = create_engine('sqlite:///Zadanie_6_3_1.db', echo=True)
meta = MetaData()

clean_station = Table(
    'clean_station', meta,
    Column('record_id',BigInteger().with_variant(Integer, "sqlite"),primery_key=True, autoincrement=True),
    Column('station',String),
    Column('date',String),
    Column('precip',Float),
    Column('tobs', Integer),
    Column('latitude',String), 
    Column('longitude', String),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String)

    )

meta.create_all(engine)
print(engine.table_names())



if __name__== '__main__':
    print("tworzenie tabeli")
    #create_table()