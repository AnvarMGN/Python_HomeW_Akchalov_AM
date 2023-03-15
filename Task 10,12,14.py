#Задача 10: 
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# input: 5 -> 1 0 1 1 0
# output: 2
"""
num_of_coins = int(input("Inter a number of coins: "))
count_side_reshko = 0
count_side_eagle = 0

for _ in range(num_of_coins):
    side_coins = int(input("Inter 0 or 1, please: "))
    # if side_coins > 1: print("Inter number 0 or 1: ")
    # else:
    if side_coins == 0:
        count_side_reshko += 1
    else:
        count_side_eagle += 1

if count_side_eagle > count_side_reshko: print(count_side_reshko)
else: print(count_side_eagle)
# result = count_side_reshko if count_side_eagle > count_side_reshko else count_side_eagle
# print(result)
"""
#Задача 12: 
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3
""""
sum = int(input("Enter the sum of the two number : "))
prod = int(input("Enter the product of the two number: "))
x = 0
y = 0

for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == sum and x * y == prod: print(x , y)
"""
#Задача 14: 
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

#10 -> 1 2 4 8
"""
n = int(input("Enter a number N: "))
result = 1

while n >= result :
    result = result * 2
    n -= 1
    print(result)
"""