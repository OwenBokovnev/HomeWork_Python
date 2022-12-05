import DB_reader as read


def menu_for_user():
    choice_admin = int(input('1. Чтение БД.\nВаш выбор: '))
    if choice_admin == 1:
        read.db_reader()

# menu_for_user()