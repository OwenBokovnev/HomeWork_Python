import sqlite3
import DB_reader as reader

def delete_record():
    try:
        sqlite_connection = sqlite3.connect('DBofficetech.db')
        cursor = sqlite_connection.cursor()
        
        reader.db_reader() # вызов просмотра перед удалением
        
        choice_delete = int(input('Введите id наименования материальных ценностей для удаления: '))

        sql_delete_query = f"""DELETE from DBofficetech where id = {choice_delete}"""
        cursor.execute(sql_delete_query)
        
        del_notification = input(f'Вы уверены, что хотите удалить запись с id = {choice_delete}? y/n ')
        if del_notification == 'y':
            sqlite_connection.commit()
            print("Запись успешно удалена")
            
            reader.db_reader()
            
            cursor.close()
        else:
            print("Данные не сохранены!")
            cursor.execute("SELECT * FROM DBofficetech")
            result = cursor.fetchall()
            print(result)

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")

# delete_record()