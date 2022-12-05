import DB_administrator_menu as admin
import DB_user_menu as user


choice_start = int(input('Выберите роль: АДМИНИСТРАТОР (1) ПОЛЬЗОВАТЕЛЬ (2): '))

if choice_start == 1:
    password = int(input('Введите пароль: '))
    if password != 123456:
        print('Пароль НЕ ВЕРЕН!')
    else:
        print('Пароль верен!')
        admin.menu_for_administrator()

elif choice_start == 2:
    user.menu_for_user()