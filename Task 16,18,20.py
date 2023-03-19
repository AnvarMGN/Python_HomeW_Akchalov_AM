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