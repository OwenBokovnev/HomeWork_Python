# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# import time

# def factorisation(n):
#    i = 2
#    primfac = []
#    while i * i <= n:
#        while n % i == 0:
#            primfac.append(i)
#            n = n / i
#        i = i + 1
#    if n > 1:
#        primfac.append(n)
#    return primfac

# try:
#     a = int(input('Программа для разложения натурального числа на простые множители.\nВведите натуральное число N: '))
#     start_time = time.time()
#     print(f'Простые множители введенного числа "{a}": {factorisation(a)}')
#     print("--- %s seconds ---" % (time.time() - start_time))
# except:
#     print(f'НЕВЕРОЯТНО, но число "{a}" не подлежит факторизации!')
   

# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

# def find_unrepeat_numbers(i):
#     for i in range (len(spicok)):
#         counter = spicok.count(spicok[i])
#         if counter == 1:
#             print(spicok[i])
        

# spicok = list(map(float, input('Введите числа списка через пробел: ').split()))
# print(f'Уникальные числа в списке: ')
# find_unrepeat_numbers(spicok)


# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



# задача 4 необязательная. Найдите корни квадратного уравнения, уравнение вводит через строку пользователь. 
# например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения. 
# Предусмотреть все варианты, сделать обработку исключений.



# задача 5 необязательная Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа. 
# Тема чат-бота любая. Просьба - постараться не использовать простой одномерный список или простой одномерный словарь.