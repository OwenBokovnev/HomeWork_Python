import sqlite3

def db_create():
    connection = sqlite3.connect('DBofficetech.db')
    cursor = connection.cursor() #cursor для одновременного использования нескольких операторов sql
    cursor.execute('''CREATE TABLE IF NOT EXISTS DBofficetech 
               (id INTEGER PRIMARY KEY, Name TEXT, Year INTEGER, Category TEXT, Price FLOAT, Amount INTEGER)''')
    connection.commit()
    connection.close
