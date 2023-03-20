# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
"""
n_len = int(input("Enter the size of the list: "))
x_find = int(input("Enter the desired number: "))

My_List_A = list()
num_count = 0

for i in range(n_len):
    My_List_A.append(int(input("Enter a value: "))) 
    # My_List_A = [i for i in range(1, n_len+1)]
    if My_List_A[i] == x_find: 
        num_count += 1

print(n_len)
print(My_List_A)
print(x_find)
print(f"-> {num_count}")
"""
# Задача 18: 
# Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

# В решении нахожу разницу по модулю diff между i-м элементом и заданным х.
# На той итерации, где эта разница меньше, запоминаю i-й элемент.
# Единственное, преобразование отрицального diff, сделано умножением на -1.
# Актуально только для натуральных чисел.
"""
n_len = int(input("Enter the size of the list: "))
x_find = int(input("Enter a number: "))

My_List_A = list()
right_num = 0
diff = x_find

for i in range(n_len):
    My_List_A.append(int(input("Enter a value: "))) 
    temp = My_List_A[i] - x_find
    if temp < 0: 
        temp *= -1
    if temp < diff: 
        diff = temp
        right_num = My_List_A[i]

print(n_len)
print(My_List_A)
print(x_find)
print(f"-> {right_num}")
"""

# *Задача 20: * 
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков.

# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12
"""
my_dict = {
'А': 1 , 'В': 1 , 'Е': 1 , 'И': 1 , 'Н': 1 , 'О': 1 , 'Р': 1 , 'С': 1 , 'Т': 1 , 
'A': 1 , 'E': 1 , 'I': 1 , 'O': 1 , 'U': 1 , 'L': 1 , 'N': 1 , 'S': 1 , 'T': 1 , 'R': 1 , 
'Д': 2 , 'К': 2 , 'Л': 2 , 'М': 2 , 'П': 2 , 'У': 2 , 
'D': 2 , 'G': 2 ,
'Б': 3 , 'Г': 3 , 'Ё': 3 , 'Ь': 3 , 'Я': 3 , 
'B': 3 , 'C': 3 , 'M': 3 , 'P': 3 ,
'Й': 4 , 'Ы': 4 , 
'F': 4 , 'H': 4 , 'V': 4 , 'W': 4 , 'Y': 4 ,
'Ж': 5 , 'З': 5 , 'Х': 5 , 'Ц': 5 , 'Ч': 5 , 
'K': 5 ,
'Ш': 8 , 'Э': 8 , 'Ю': 8 , 
'J': 8 , 'X': 8 ,
'Ф': 10, 'Щ': 10, 'Ъ': 10 ,
'Q': 10 , 'Z': 10 
}

word = input('Enter one word: ').upper() # использую функцию upper, т.к. в словаре только заглавные буквы
resalt = 0

for letter in word:
    for key in my_dict:
        if letter == key:
            resalt += my_dict[key]

print(resalt)
"""