import json
import pprint

from easygui import *


def write_inf(dota, file_name):
    with open(file_name, encoding="utf-8") as file:
        data = json.load(file)
        data['users'].append(dota)
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

def save_inf(dota, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(dota, f, ensure_ascii=False, indent=4)


def read_inf(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def change_inf(n,value):
    if n == 0:
        value['name'] = enterbox(
            msg="Введите новое имя", title="Новое имя пользователя")
        data = read_inf('phonebook.json')
        write_inf(value, 'phonebook.json')
    if n == 1:
        value['phonenumber'] = enterbox(
            msg="Введите новый номер телефона",
            title="Новый номер телефона")
        data = read_inf('phonebook.json')
        write_inf(value, 'phonebook.json')
    if n == 2:
        data = read_inf('phonebook.json')
        write_inf(value, 'phonebook.json')

def change_contacts_menu():
    m = indexbox(msg="Контакт успешно изменен.", title="Контакт изменен",
                 choices=("Изменить еще", "Завершить", "Главное меню"))
    if m == 0:
        start_prog(5)
    elif m == 1:
        start_prog(6)
    elif m == 2:
        starter()


title = "Телефонный справочник"
choices = ['Добавить запись', 'Посмотреть все записи',
           'Найти контакт','Удалить контакт', 'Изменить контакт', 'Выйти']


def starter():
    reply = choicebox("Добро пожаловать, что вы хотите сделать?", title=title,
                      choices=choices)
    if reply == 'Добавить запись':
        n = 1
    elif reply == 'Посмотреть все записи':
        n = 2
    elif reply == 'Найти контакт':
        n = 3
    elif reply == 'Удалить контакт':
        n = 4
    elif reply == 'Изменить контакт':
        n = 5
    elif reply == 'Выйти':
        n = 6
    start_prog(n)


def start_prog(num):
    if num == 1:
        username = enterbox("Введите имя: ", title="Введите имя")
        phonenumber = enterbox("Введите номер телефона: ", title="Введите номер телефона")
        print(list)
        data = read_inf('phonebook.json')
        for user in data['users']:
            if user['name'] == username:
                n = indexbox(
                    msg="Пользователь с таким именем есть!",
                    title="Такой контакт есть!", choices=("Повторить", "Главное меню"))
                if n == 0:
                    start_prog(1)
                    continue
                if n == 1:
                    starter()
                    continue
            elif user['phonenumber'] == phonenumber:
                n = indexbox(
                 msg="Такой номер телефона есть",
                 title="Такой контакт есть!",
                 choices=("Повторить", "Главное меню"))
                if n == 0:
                    start_prog(1)
                    continue
                if n == 1:
                    starter()
                    continue
        new_dota = {
            'name': username,
            'phonenumber': phonenumber}
        write_inf(new_dota, 'phonebook.json')
        finder = indexbox(msg="Контакт успешно добавлен, "
                              "хотите добавить следующего пользователя?",
                          title="Контакт добавлен", choices=("Да", "Завершить",
                                                             "Главное меню"))
        if finder == 0:
            start_prog(1)
        if finder == 1:
            start_prog(6)
        if finder == 2:
            starter()

    elif num == 2:
        users = read_inf('phonebook.json')
        pretty_print = pprint.pformat(users)
        finder = indexbox(msg=pretty_print, title="Список контактов",
                          choices=("Завершить", "Главное меню"))
        if finder == 0:
            start_prog(6)
        if finder == 1:
            starter()
    elif num == 3:
        find = enterbox("Введите имя или номер телефона: ")
        users = read_inf('phonebook.json')
        flag = False
        for user in users['users']:
            if user['name'] == find:
                flag = True
            elif user['phonenumber'] == find:
                flag = True
        if flag:
            for user in users['users']:
                if user['name'] == find:
                  finder = indexbox(msg=f"Имя: {user['name']}\nНомер телефона: {user['phonenumber']}", title="Поиск контакта",
                     choices=("Найти еще", "Завершить", "Главное меню"))
                  if finder == 0:
                      start_prog(3)
                  elif finder == 1:
                      msgbox("До свидания")
                  elif finder == 2:
                      starter()
                elif user['phonenumber'] == find:
                    finder = indexbox(msg=user,
                                      title="Поиск контакта",
                                      choices=("Найти еще", "Завершить",
                                      "Главное меню"))
                    if finder == 0:
                        start_prog(3)
                    elif finder == 1:
                        start_prog(6)
                    elif finder == 2:
                        starter()
        if not flag:
            finder = indexbox(msg="Такого контакта нет\nХотите попробовать еще?",
                      title="Поиск контакта",
                              choices=("Да", "Завершить", "Главное меню"))
            if finder == 0:
                start_prog(3)
            if finder == 1:
                start_prog(6)
            if finder == 2:
                starter()
    elif num == 4:
        find = enterbox("Введите имя или номер телефона: ")
        data = read_inf('phonebook.json')
        mininal = 0
        flag = False
        for user in data['users']:
            if user['name'] == find:
                flag = True
            elif user['phonenumber'] == find:
                flag = True
        if flag:
            for user in data['users']:
                if user['name'] == find:
                    data['users'].pop(mininal)
                    save_inf(data, 'phonebook.json')
                    msgbox("Контакт успешно удален!")
                elif user['phonenumber'] == find:
                    data['users'].pop(mininal)
                    save_inf(data, 'phonebook.json')
                    msgbox("Контакт успешно удален!")
                else:
                    None
                    mininal = mininal + 1
        if not flag:
            msgbox("Такого контакта нет!")

        finder = indexbox(msg="Желаете продолжить?", title="Удаление контакта",
                          choices=("Удалить еще", "Главное меню", "Завершить"))
        if finder == 0:
            start_prog(4)
        if finder == 1:
            starter()
        if finder == 2:
            start_prog(6)
    elif num == 5:
        find = enterbox("Введите имя или номер телефона: ")
        data = read_inf('phonebook.json')
        mininal = 0
        flag = False
        for user in data['users']:
            if user['name'] == find:
                flag = True
            elif user['phonenumber'] == find:
                flag = True
        if flag:
            for user in data['users']:
                if user['name'] == find:
                    value = data['users'].pop(mininal)
                    save_inf(data, 'phonebook.json')
                    n = indexbox(msg=f"Найден контакт {value}, "
                    f"что вы хотите изменить?", choices=("Имя", "Номер телефона", "Главное меню"))
                    change_inf(n, value)
                    if n == 2:
                        starter()
                    change_contacts_menu()
                elif user['phonenumber'] == find:
                    value = data['users'].pop(mininal)
                    save_inf(data, 'phonebook.json')
                    n = indexbox(msg=f"Найден контакт {value}, "
                        f"что вы хотите изменить?", choices=(
                        "Имя", "Номер телефона", "Главное меню"))
                    change_inf(n, value)
                    if n == 2:
                        starter()
                    change_contacts_menu()
                else:
                    None
                    mininal = mininal + 1
        if not flag:
            msgbox("Такого контакта нет!")
    elif num == 6:
        msgbox("Пока")

    else:
        print("Ввели неверное значение, начните заного")


starter()

