import sqlite3
import DB_reader as reader


def db_update():
    reader.db_reader()
    command_id = int(input('Введите ID оборудования для редактирования": '))
    command_pole = input('Введите поле для редактирования": ')
    command_value = input('Введите данные для сохранения": ')

    connection = sqlite3.connect('DBofficetech.db')
    cursor = connection.cursor()
    
    cursor.execute(f"UPDATE DBofficetech SET {command_pole}={command_value} WHERE id = {command_id}")
    commit = input('Сохранить изменения? y/n: ')
    if commit == 'y':
        connection.commit()
        print("Запись успешно вставлена ​​в таблицу DBofficetech", cursor.rowcount)
        cursor.execute("SELECT * FROM DBofficetech")
        result = cursor.fetchall()
        connection.close()
        reader.db_reader()
    else:
        print("Данные не сохранены!")
        cursor.execute("SELECT * FROM DBofficetech")
        result = cursor.fetchall()
        print(result)
        connection.close()
        reader.db_reader()
        
