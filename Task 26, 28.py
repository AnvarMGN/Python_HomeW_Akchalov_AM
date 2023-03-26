# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

# код без учёта отрицательной степени. 
'''
def exponentiation(a, b):
    if b == 1: # возвращаем а, когда степерь b равна 1
        return a
    return exponentiation(a, b - 1) * a

a = int(input('Enter a basic: '))
b = int(input('Enter a degree: '))

print(exponentiation(a,b))
'''

# Задача 28:

# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1) 

a = int(input('Enter the number A: '))
b = int(input('Enter the number B: '))

print(sum(a,b))