####### ЗАДАЧА 1 ########
####### Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# n = int(input("Введите число дня недели от 1 до 7, где 1 - понедельник: "))
# if n in range (1, 6):
#     print("Введенный день НЕ ВЫХОДНОЙ")
# elif n == 6 or n == 7:
#     print("Введенный день ВЫХОДНОЙ")
# else:
#     print("Введенное число вне допустимого диапазона.")

####### ЗАДАЧА 2 ########
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")

####### ЗАДАЧА 3 ########
####### Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# x = int(input("Введите координату X точки: "))
# y = int(input("Введите координату Y точки: "))

# if x > 0 and y > 0:
#     print("Точка находится в I четверти")
# elif x < 0 and y > 0:
#     print("Точка находится во II четверти")
# elif x < 0 and y < 0:
#     print("Точка находится в III четверти")
# elif x > 0 and y < 0:
#     print("Точка находится во IV четверти")
# else:
#     print("Точка находится в центре")

####### ЗАДАЧА 4 ########
####### Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div,

# a = int(input("Введите первое число: "))
# action = input("Действие: ")
# b = int(input("Введите второе число: "))

# if action == "+":
#     print(a, '+', b, '=', a + b)
# elif action == "/" and b == 0:
#     print("Деление на 0!")
# elif action == "-":
#     print(a, '+', b, '=', a - b)
# elif action == "/":
#     print(a, '/', b, '=', a / b)
# elif action == "*":
#     print(a, '*', b, '=', a * b)
# elif action == "mod":
#     print(a, '%', b, '=', a % b)
# elif action == "pow":
#     print(a, '^', b, '=', a ** b)
# elif action == "div":
#     print(a, 'div', b, '=', a // b)
# else:
#     print("Недоступное действие!")

####### ЗАДАЧА 5 ########
####### Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# def show_array(array):
#     for i in range(len(array)):
#         for j in range(len(array)):
#             print(array[i][j], end = ' ')
#         print()

array = [[10, 4, -7, 3], [18, 5, 6, 9], [1, -9, 4, 2], [7, 18, -4, 7]]
print(*array, sep = '\n')
# show_array(array)
new_array = []
for i in array:
    for i2 in i:
        new_array.append(i2)
array = sorted(new_array)
print('\nОтсортированный массив: ')
for x in range(0, len(array), 4):
    e_c = array[x : 4 + x]
    if len(e_c) < 4:
        e_c = e_c + [None for y in range(len(e_c))]
    print(list(e_c))