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

def select_function():
    while True:
        command = input('Введите команду(add /read /find /del /change /q): ')
        if command == 'add':
            write_file()
        elif command == 'read':
            read_file()
        elif command == 'find':
            find_file()
        elif command == 'del':
            delete_file()
        elif command == 'change':
            pass
        elif command == 'q': 
            break
        

def write_file():
    with open(file_path, 'a', encoding = 'UTF-8') as f:
        f.writelines('\n' + input("Введите ФИО и телефон:"))

def read_file():
    with open(file_path, 'r', encoding = 'UTF-8') as f:
        for line in f:
            print(line.strip())

def find_file():
    find_contact = input("Ввведите Имя или Фамилию: ")
    with open(file_path,'r',encoding = 'UTF-8') as f:
        for line in f:
            if find_contact.casefold() in line.casefold():
                print(line)

def delete_file():
    with open("telephon_list.txt",'w',encoding = 'UTF-8') as f:
        pass
            

file_path = r'telephon_list.txt'

select_function()