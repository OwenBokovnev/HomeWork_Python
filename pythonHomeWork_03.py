# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_elements_odd_positions(sum):
#     sum = 0
#     for i in range(len(spicok)):
#         if i % 2 == 1:
#             sum += spicok[i]
#             i += 1
#     return sum

# def find_odd_positions(i):
#     for i in range(len(spicok)):
#         if i % 2 == 1:
#             print (f'На нечетной позиции с индексом {[i]} элемент: {spicok[i]}')

# try:
#     spicok = list(map(int, input('Введите значения чисел через пробел: ').split()))
#     find_odd_positions(spicok)
#     print(f'Сумма нечетных элементов масива равна: {sum_elements_odd_positions(spicok)}')
# except:
#     print('Среди введенных элементов есть не число!')

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def getting_pairs_of_elements(i):
#     if int(len(spicok)) % 2 == 1:
#         size = int(len(spicok)/2 + 1)
#         for i in range(size):
#             print (f'Произведение {i+1} пары элементов {spicok[i]} и {spicok[-i - 1]} равно: {spicok[i] * spicok[-i - 1]}')
#     else:
#         size = int(len(spicok)/2)
#         for i in range(size):
#             print (f'Произведение {i+1} пары элементов {spicok[i]} и {spicok[-i - 1]} равно: {spicok[i] * spicok[-i - 1]}')

# spicok = list(map(int, input('Введите числа через пробел: ').split()))
# print(f'Введенный массив: {spicok}')
# getting_pairs_of_elements(spicok)

# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from decimal import Decimal

# def separate_main_part(result):
#     new_spicok = []
#     counter = 0
#     size = int(len(spicok))
#     for i in range (size):
#         result = Decimal(str(spicok[i])) % 1
#         print (result)
#         new_spicok.insert(counter, float(Decimal(str(spicok[i])) % 1))
#     return(new_spicok)

# def find_max_min_value(i):
#     size = int(len(new_spicok))
#     for i in range (size):
#         max = new_spicok[i]
#         min = new_spicok[i]
#         for i in range (size):
#             if new_spicok[i] < min:
#                 min = new_spicok[i]
#             elif new_spicok[i] > max:
#                 max = new_spicok[i]
#     return print (f'Разница между максимальным и минимальным значениями равна: {max} - {min} = {max - min}')

# spicok = list(map(float, input('Введите числа c дробной частью через пробел: ').split()))
# print(f'Введенный список выглядит так: {spicok}')

# new_spicok = separate_main_part(spicok)

# print(f'Новый список выглядит так: {new_spicok}')
# print('----------------')
# find_max_min_value(new_spicok)


# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input('Введите целое число: '))
b = ''
while a > 0:
    b = str(a % 2) + b
    a = a // 2
 
print(f'В двоичной сисстеме счисления введенное число будет равно: {b}')


# Задача 5. HARD необязательная.Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры), 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место 
# и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.

