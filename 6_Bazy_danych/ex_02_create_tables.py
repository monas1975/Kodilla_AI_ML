#ex_02_create_tables.py

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

def add_project(conn, project):
    """
    Create a new project into the projects table
   :param conn:
   :param project:
   :return: project id
    """
    sql = ''' INSERT INTO  projects(nazwa, start_date, end_date)
                VALUES(?,?,?)'''
    
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def add_task(conn, project):
    """
    Create a new project into the projects table
   :param conn:
   :param task:
   :return: task id
    """
    sql = ''' INSERT INTO tasks(project_id, nazwa, opis, status, start_date, end_date)
                VALUES(?,?,?,?,?,?)'''
    
    cur = conn.cursor()
    cur.execute(sql,task)
    conn.commit()
    return cur.lastrowid



if __name__ == "__main__":

    create_project_sql = """
    -- projects table
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        nazwa text NOT NULL,
        start_date text,
        end_date text

    );
    """

    create_task_sql = """
    -- zadanie table
    CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY,
    project_id integer NOT NULL,
    nazwa VARCHAR(250) NOT NULL,
    opis TEXT,
    status VARCHAR(15) NOT NULL,
    start_date text NOT NULL,
    end_date text NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

db_file = "database.db"

conn = create_connection(db_file)
if conn is not None:
    execute_sql(conn, create_project_sql)
    execute_sql(conn, create_task_sql)
    

    project = ("Pompki", "2020-05-12 00:00:00", "2020-05-14 00:00:00")
    pr_id = add_project(conn, project)

    task = (pr_id,
            "Pompki",
            "4 x 25",
            "ended",
            "2020-05-12 12:00:00",
            "2020-05-12 15:00:00")
    task_id = add_task(conn,task)
    print(pr_id,task_id)
    conn.commit()


    conn.close()