# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
"""
n = int(input("Enter a number n: "))
m = int(input("Enter a number m: "))
List_n = []
List_m = []

for i in range(n):
    temp = int(input("Enter a number for list 1: "))
    List_n.append(temp)
print()

for i in range(m):
    temp = int(input("Enter a number for list 2: "))
    List_m.append(temp)
print()

resalt = sorted(set(List_n).intersection(set(List_m)))

print(n, m)
print(List_n)
print(List_m)
print (resalt)
"""

# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

count_bush = int(input("Enter the number of bushes: "))
dict_bush = {}

for bush in range(count_bush):
    dict_bush[bush] = int(input("Enter a prodyctiviti: "))
print(dict_bush)

resalt = 0
for bush in range(count_bush):
    if bush == 0:
        prod = dict_bush[0] + dict_bush[1] + dict_bush[3]
        if prod > resalt:
            resalt = prod
    if bush == 1:
        prod = dict_bush[1] + dict_bush[2] + dict_bush[0]
        if prod > resalt:
            resalt = prod
    if bush == 2:
        prod = dict_bush[2] + dict_bush[1] + dict_bush[3]
        if prod > resalt:
            resalt = prod
    if bush == 3:
        prod = dict_bush[3] + dict_bush[0] + dict_bush[2]
        if prod > resalt:
            resalt = prod
print(resalt)
    