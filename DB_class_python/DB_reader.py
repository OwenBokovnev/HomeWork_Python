import sqlite3

def db_reader():
    print('\nНа текущий момент зарегистрированы мат.средства:\n')
    connection = sqlite3.connect('DBofficetech.db')
    cursor = connection.cursor()
    
    cursor.execute('PRAGMA table_info("DBofficetech")')
    column_names = [i[1] for i in cursor.fetchall()]
    print(column_names)
    
    cursor.execute("SELECT * FROM DBofficetech")
    rows = cursor.fetchall()
    
    for row in rows:
        print (row)

    
# db_reader()




