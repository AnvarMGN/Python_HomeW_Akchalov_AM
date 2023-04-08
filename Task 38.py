# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.

# 1. Программа должна выводить данные

# 2. Программа должна сохранять данные в текстовом файле

# 3. Пользователь может ввести одну из характеристик для поиска определенной 
# записи(Например имя или фамилию человека)

# 4. Использование функций. Ваша программа не должна быть линейной

# def select_function():
#     while True:
#         command = input('Введите команду(add /read /find /del /change /q): ')
#         if command == 'add':
#             write_file()
#         elif command == 'read':
#             read_file()
#         elif command == 'find':
#             find_file()
#         elif command == 'del':
#             delete_file()
#         elif command == 'change':
#             change_file()
#         elif command == 'q': 
#             break
        

# def write_file():
#     with open(file_path, 'a', encoding = 'UTF-8') as f:
#         f.writelines('\n' + input("Введите ФИО и телефон:"))

# def read_file():
#     with open(file_path, 'r', encoding = 'UTF-8') as f:
#         for line in f:
#             print(line.strip())

# def find_file():
#     find_contact = input("Ввведите Имя или Фамилию: ")
#     with open(file_path,'r',encoding = 'UTF-8') as f:
#         for line in f:
#             if find_contact.casefold() in line.casefold():
#                 print(line)

# def delete_file():
#     with open(file_path, 'r', encoding = 'UTF-8') as f:
#         lines = f.readlines()
#     with open(file_path, 'w', encoding = 'UTF-8') as f:
#         for line in lines:
#             if line.find('Иванов') == -1:
#                 f.write(line)
            
# def change_file():
#     with open(file_path, 'r', encoding = 'UTF-8') as f:
#         old_list = f.read()
        
#         new_list = old_list.replace(input('Введите ФИО и телефон: ') + '\n', input('Введите ФИО и телефон 2: '))
        
#     with open(file_path, 'w', encoding = 'UTF-8') as f:
#         f.write(new_list)
        

# file_path = r'telephon_list.txt'

# select_function()
# ==============================================================================================
import pickle

def add_contact():
    with open(file_path, 'w') as f:
        pickle.dump(telephon_book,file_path)
    # telephon_book[0] = 'Иванов', 'Иван', 'Иванович', '+79093428844'
    # telephon_book[1] = 'Петров', 'Петр', 'Петрович', '+78983428888'
    # telephon_book[2] = 'Сидоров', 'Сидр', 'Сидорович', '+789839893333'
    print(f'Количесво записей: {len(telephon_book)}')
    telephon_book[int(input('№: '))] = input('Фамилия: '), input('Имя: '), input('Отчество: '), input('Телефон: ')
    with open(file_path, 'a', encoding = 'UTF-8') as f:
        f.writelines('\n' + str(telephon_book))


def read_contact():
    print(telephon_book)

def find_contact(dictionary, searchString):
    return {key:val for key,val in dictionary.items() if any(searchString in s for s in val)}

def delete_contact(dictionary, searchString):
    print({key:val for key,val in dictionary.items() if any(searchString in s for s in val)})
    telephon_book.pop(int(input('Удаление записи. Введите номер строки: ')))
    print(dictionary)

def change_contact(dictionary, searchString):
    print({key:val for key,val in dictionary.items() if any(searchString in s for s in val)})
    print('Введите новые данные. ФИО и номер записи: ')
    telephon_book[int(input('№ записи: '))] = input('Фамилия: '), input('Имя: '), input('Отчество: '), input('Телефон: ')
    print(dictionary)

def select_function():
    while True:
        command = input('Введите команду("1"-Добавление /"2"-Чтение /"3"-Поиск /"4"-Удаление /"5"-Изменение /"0"-Выход"):')
        if command == '1':
            add_contact()
        elif command == '2':
            read_contact()
        elif command == '3':
            print(find_contact(telephon_book, input('Поиск записи. Введите ФИО: ')))
        elif command == '4':
            delete_contact(telephon_book, input('Удаление записи. Введите ФИО: '))
        elif command == '5':
            change_contact(telephon_book, input('Редактирование записи. Введите ФИО: '))
        elif command == '0': 
            break

file_path = r'telephon_list.txt'
telephon_book = {}

select_function()


