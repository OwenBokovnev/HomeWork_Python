import DB_insert as ins
import DB_reader as read
import DB_sqlite_CREATE as create
import DB_update as update
import DB_delete_record as delete

def menu_for_administrator():
    choice_admin = int(input('\nМеню АДМИНИСТРАТОРА\n1. Редактирование позиций в БД\n2. Чтение БД.\n3. Добавление новых материальных ценностей в БД\n4. Удаление записи\n5. Создание БД\nВаш выбор: '))
    if choice_admin == 2:
        read.db_reader()
    elif choice_admin == 3:
        ins.db_insert()
    elif choice_admin == 4:
        delete.delete_record()
    elif choice_admin == 1:
        update.db_update()
    elif choice_admin == 5:
        create.db_create()