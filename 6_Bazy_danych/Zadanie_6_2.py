# Zadanie 6_2
import sqlite3
from sqlite3 import Error

#Tworzenie połaczenia
def create_connection(db_file):
 """ create a database connection to the SQLite database
       specified by the db_file
   :param db_file: database file
   :return: Connection object or None
   """
 conn = None
 try:
        conn = sqlite3.connect(db_file)
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
#Funkcja tworzaca tebele na potrzeby zadania

def create_all_tables(db_file):
   conn = create_connection(db_file)
   create_departments_sql = """
    -- department table
    CREATE TABLE IF NOT EXISTS departments (
        Department_id integer PRIMARY KEY,
        Department text NOT NULL,
        Description text

    );
    """
   create_employees_sql = """
    -- employess table
    CREATE TABLE IF NOT EXISTS employees (
        Employee_id integer PRIMARY KEY,
        FirstName text NOT NULL,
        LastName text NOT NULL,
        PersonalNumber text,
        Mail text,
        Telephone text,
        Department_id integer NOT NULL,
        Position_id integer NOT NULL,
        Boss_id integer,
        Employment_start_date text,
        Salary real,
        FOREIGN KEY (Department_id) REFERENCES projects (id),
        FOREIGN KEY (Position_id) REFERENCES projects (id)

    );
    """
   create_position_sql = """
    -- department table
    CREATE TABLE IF NOT EXISTS positions (
        Position_id integer PRIMARY KEY,
        Position text NOT NULL,
        Description text

    );
    """
   if conn is not None:
      execute_sql(conn, create_departments_sql)
      execute_sql(conn, create_position_sql)
      execute_sql(conn, create_employees_sql)
      conn.close()

def insert_position(conn, position):   
    """
    Create a new project into the projects table
   :param conn:
   :param position:
   :return: project id
    """
    sql = ''' INSERT INTO  positions(position, description)
                VALUES(?,?)'''
    
    cur = conn.cursor()
    cur.execute(sql, position)
    conn.commit()
    return cur.lastrowid

def insert_department(conn, department):   
    """
    Create a new department into the deprtment table
   :param conn:
   :param department:
   :return: department id
    """
    sql = ''' INSERT INTO  departments(department, description)
                VALUES(?,?)'''
    
    cur = conn.cursor()
    cur.execute(sql, department)
    conn.commit()
    return cur.lastrowid

def insert_employees(conn, employee):
   """
    Create a new employee into the employees table
   :param conn:
   :param employee:
   :return: employee id
    """
   sql = """INSERT INTO employees(FirstName, LastName, PersonalNumber,Mail,Telephone,Department_id,Position_id, Boss_id,Employment_start_date, Salary)
                VALUES(?,?,?,?,?,?,?,?,?,?)
            """
   cur = conn.cursor()
   cur.execute(sql, employee)
   conn.commit()
   return cur.lastrowid   

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
        #print("jestem w petli")
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    
    print(f"SELECT * FROM {table} WHERE {q}", values)
    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall()

    return rows

def update_employees(conn, table, Employees_id, **kwargs):
 """
   update status, begin_date, and end date of a task
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
 parameters = [f"{k} = ?" for k in kwargs]
 parameters = ", ".join(parameters)
 values = tuple(v for v in kwargs.values())
 values+=(Employees_id, )
 print(Employees_id)
 print(values)
 sql = f''' UPDATE {table}
            SET {parameters}
            WHERE Employee_id = ? '''
 try:
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("OK")
 except sqlite3.OperationalError as e:
         print(e)

def delete_where(conn, table, **kwargs):
    """
   Delete from table where attributes from
   :param conn:  Connection to the SQLite database
   :param table: table name
   :param kwargs: dict of attributes and values
   :return:
   """
    qs=[]
    values=tuple()
    for k,v in kwargs.items():
        qs.append(f"{k}=?")
        values +=(v,)
    q = " AND".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("Deleted")

def delete_all(conn, table):
    """
   Delete all rows from table
   :param conn: Connection to the SQLite database
   :param table: table name
   :return:
   """
    sql = f'DELETE FROM {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print("Deleted")

def delete_where(conn, table, **kwargs):
    """
   Delete from table where attributes from
   :param conn:  Connection to the SQLite database
   :param table: table name
   :param kwargs: dict of attributes and values
   :return:
   """
    qs=[]
    values=tuple()
    for k,v in kwargs.items():
        qs.append(f"{k}=?")
        values +=(v,)
    q = " AND".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("Deleted")
 

if __name__ == "__main__":
  #tworzenie tabel
  create_all_tables("zadanie_6_1.db")
  #ustanowienie polaczenia do BD
  conn = create_connection("zadanie_6_1.db")
  #pozycje do wprowadzenia
  position = [ ("prezes", "Prezes"), 
             ("wprezes", "Vice Prezes"),
             ("kierownik", "Kierownik"),
             ("analityk", "Analityk"),
             ("asystent", "Asysteny"),
              ("archiwista","Archiwista"),
              ("fakturzysta", "Fakturzyta"),
              ("kadrowa", "Kadrowa"),
              ("gksiegowa", "Głowna Księgowa"),
              ("księgowa", "Księgowa"),
              ("ganalityk", "Główny Analityk")]
                                       
   #wprowadzenie stanowisk do BD   
  print("wprowadzam stanowiska")        
  for item in position:
     print("Wprowadzam: " + str(item))
     position = item
     insert_position(conn, position)
     conn.commit()
    

    # wprowadzenie wydziałow
  departments = [("zarzad", "Zarząd"),
           ("kierownicza","Kadra Kierownicza"),
           ("dsprzedazy", "Dział Sprzedaży"),
           ("dkadr", "Dział Kadr"),
           ("dmarketing", "Dział Marketingu")
           ]
  print("wprowadzam wydiały")
  for item in departments:
        print("Wprowadzam: " + str(item))
        department = item
        insert_department(conn, department)
        conn.commit()

  print("wprowadzam pracowników")
    #wprowadzenie  pracowników
  employees = [
        ("Adam", "Adamski", "A561","a_adamski@abc.com","+48 222 111 111", 1,1,'',"01-01-2001",50000.99 ),
        ("Bartosz", "Baranski", "A562","b_baranski@abc.com","+48 222 111 112", 1,1,1,"01-01-2011", 35000.11 ),
        ("Magdalena", "Nawrocka", "A563","m_nawrocka@abc.com","+48 222 111 113", 3,9,1,"01-01-2016", 21000.11 ),
        ("Barbara", "Bartoszewsak", "A564","b_bartoszewskaa@abc.com","+48 222 111 114", 3,10,1,"01-01-2016", 21000.11 )

    ]
  for item in employees:
        print("Wprowadzam: " + str(item))
        employee = item
        insert_employees(conn, employee)
        conn.commit()
    
  print("----- SELECT ALL   ------ ")
  print(select_all(conn, "employees"))

  print(" ---------- SELECT WHERE")
  print(select_where(conn, "employees", Employee_id=2))
  print(select_where(conn, "employees", FirstName = "Barbara"))
  #print(select_where(conn, "employees", Salary =  >50000.00))

  print("-----SELECT UPDATE -------")
  update_employees(conn, "employees", 2 ,FirstName="Bartosz")
  update_employees(conn, "employees", 2 ,FirstName="Bartosz")
  update_employees(conn, "employees", 4 ,Salary= 12000)


  print("____ DELATE ALL _____")
  #delete_all(conn, "employees")

  print("___DELATE WHERE_____")

  delete_where(conn, "Employees", Employee_id=3)
  delete_where(conn,"Positions", Position = "asystent")
  
  conn.close

  