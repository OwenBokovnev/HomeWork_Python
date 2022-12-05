import sqlite3
import DB_reader as reader


def db_insert():
    # rowid = 
    command_name = str(input('Введите НАИМЕНОВАНИЕ оборудования": '))
    command_year = int(input(f'Введите ГОД выпуска оборудования {command_name}: '))
    
    cat = int(input(f'Выберите КАТЕГОРИЮ для оборудования\n1 - Принтер\n2 - Системный блок\n3 - Монитор\n4 - Источник бесперебойного питания\n:_____'))
    if cat == 1:
        command_category = 'printer'
    elif cat == 2:
        command_category = 'sysblock'
    elif cat == 3:
        command_category = 'monitor'
    elif cat == 4:
        command_category = 'power_supply'
                    
    command_price = float(input(f'Введите СТОИМОСТЬ для {command_name}: '))
    command_amount = int(input(f'Введите КОЛИЧЕСТВО {command_name}: '))
    connection = sqlite3.connect('DBofficetech.db')
    cursor = connection.cursor()
    
    cursor.execute(f"INSERT INTO DBofficetech (id, name, year, category, price, amount) VALUES ((SELECT max(id) FROM DBofficetech) + 1,'{command_name}', {command_year}, '{command_category}', {command_price}, {command_amount})")
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
    

