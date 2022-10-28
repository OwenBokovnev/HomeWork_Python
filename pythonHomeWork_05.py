# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота

# а) Подумайте как наделить бота ""интеллектом""

# import random

# number1 = 0
# number2 = 0
# print('-----------------------')
# print('Игра Candies.\nКто забирает последнюю конфету - проиграл.')
# print('-----------------------')
# command = input("Для определения первого хода - Игрок1 нажмите 'q': ")
# if command == 'q':
#     number1 = random.randint(1,50)
#     print(f"Число для Игрока1 = :{number1}")

# command = input("Для определения первого хода - Игрок2 нажмите 'q': ")
# if command == 'q':
#     number2 = random.randint(1,50)
#     print(f"Число для Игрока1 = :{number2}")

# print(f"У Игрока1 число = {number1}, у Игрока2 число = {number2}")
# if number1 >= number2:
#     print('Начинает Игрок1.')
# else:
#     print('Начинает Игрок2.')
# print('-----------------------')

# candies = int(input('Определите число конфет в игре: '))
# candies_max = int(input('Определите максимальное количество конфет за ход: '))
# print('-----------------------\n-----------------------')
# count = 0
# candies_round = 0
# print(f'На начало игры имеется конфет: {candies} шт.')
# while True:
#     while candies_round <= candies_max:
#         candies_round = int(input(f'Итого конфет: {candies} шт.\nИгрок, сколько конфет вы возьмете? (max = {candies_max} шт.): '))
#         candies -= candies_round
#         if candies_round > candies:
#             input(print(f'Количество конфет за ход не может превышать остаток {candies}\nВведите другое значение: '))
#     else:
#         print(f'Количество конфет за ход не может превышать {candies_max}')

        

# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# import json

# f = open('rle.txt')
# line = f.readline()
# while line:
#     print (f"Данные для сжатия: {line}"),
#     count = 1
#     for i in range(len(line)-1):
#         if i <= len(line):
#             if line[i] == line[i + 1]:
#                 count += 1
#             else:
#                 a = line[i]
#                 print(count, line[i])
#                 count = 1
#     print(count, line[i])
#     result = []    
#     with open("rle_result.json", "w", encoding="utf-8") as res:
#         res.write(json.dumps(result, ensure_ascii=False))
#     print("Сжатие успешно завершено и сохранено в файле rle_result.json")
#     break
# f.close()

# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

# line = 'форматиабврование текста по шаблону абв'
# print(f'Исходный текст: {line}')
# words = line.split(' ')
# fragment = 'абв'
# new_words = []
# for word in words:
#     if fragment not in word:
#         new_words.append(word)
# new_words
# print(f"Вот, что получили: {' '.join(new_words)}")

# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9



# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:* 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 
# [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]

list = [1, 5, 2, 3, 4, 6, 1, 7]
print(f'Имеем массив: {list}')
list.sort()
list.append(0)
new_list = []
size = len(list)
for i in range(size - 1):
    if list[i + 1] == list[i] + 1:
        new_list.append(list[i + 1])
        
min = list[0]
max = list[0]
for i in range(len(new_list)):
    if new_list[i] <= min:
        min = new_list[i]
    elif new_list[i] >= max:
        max = new_list[i]
print(f'Максимальная последовательность с {min} по {max}')