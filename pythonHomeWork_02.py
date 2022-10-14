######### Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. 
# Через строку нельзя решать.

# a = float(input("Enter number: "))

# def separate(x):
#     r = [x % 10]
#     while x > 10:
#         x //= 10   
#         r.insert(0, x % 10)        
#     return r

# if a >= 1:
#     c = (a - round(a)) * 100000000000000
#     b = separate(a)
#     d = separate(c)
#     sumOfElements1 = sum(b)
#     sumOfElements2 = sum(d)
#     print("Sum of all the elements in the list is:", round(sumOfElements1) + round(sumOfElements2))
# else:
#     c = a * 100000000000000
#     b = separate(c)
#     sumOfElements2 = sum(b)
#     print("Sum of all the elements in the list is:", round(sumOfElements2))

######### Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# a = int(input("Enter number: "))
# i = 1
# multiple = 1
# while i <= a:
#     multiple = multiple * i
#     i += 1
# print(f"Result ot multiplication all digits from 1 to {a} is:", multiple)

######### Задача 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# import re

# str1 = input("Введите 1 строку: ")
# str2 = input("Введите 2 строку: ")
# counter = 0

# print(len(re.findall((str2), str1)))

######### Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, 
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

# import math

# n = int(input("Enter number of dimentions N: "))

# coordA = []
# for i in range(n):
#     coordA.append(int(input("Enter coordinates for dot A: ")))

# coordB = []
# for i in range(n):
#     coordB.append(int(input("Enter coordinates for dot B: ")))

# print(coordA, coordB)

# distant = 0
# distant2 = 0
# for i in range(n):
#     i = 1
#     distant += (coordB[i] - coordA[i])**2
#     distant2 = math.sqrt(distant)

# print(round(distant2, 3))

######### Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . 
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, проверяем это утверждение 100 раз, 
# с помощью модуля time выводим на экран , сколько времени отработала программа.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

