

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
        create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
    """
    conn = None
    try:
        conn =sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def execute_sql(conn, sql):
    """
    Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()
   return rows


def select_where(conn, table, **query):
    """
   Query tasks from table with data from **query dict
   :param conn: the Connection object
   :param table: table name
   :param query: dict of attributes and values
   :return:
   """
    cur = conn.cursor()
    qs = []
    values= ()

    for item in query:
        print(item)
  
    for k, v in query.items():
        print("jestem w petli")
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    
    print(f"SELECT * FROM {table} WHERE {q}", values)
    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall()

    return rows

if __name__ == "__main__":

 db_file = "database.db"

conn = create_connection(db_file)
if conn is not None:
    #execute_sql(conn, s)
    print(select_all(conn, "projects"))
    print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print(select_all(conn,"tasks"))
    conn.commit()
    conn.close()
    print("_____________________________________________________")

    conn = create_connection(db_file)
if conn is not None:
        
        print(select_where(conn, "tasks", status="ended"))

print("_____________________________________________________")
if conn is not None:
    print(select_where(conn, "tasks", project_id=6))

conn.commit()
conn.close()