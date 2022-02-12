from authorization import autorizate
from classes import Users
from time import localtime, strftime, sleep
import asyncio

time_string = strftime("%H:%M:%S", localtime())
datum = strftime("%d:%m:%Y", localtime())
users = []

#this is my fucking branch, bitch!

def main():
    if autorizate():
        user_add()
        transaction(users[0])
        user_status()

def user_add():
    login = 'Lex'
    User_Autorizate = True
    if User_Autorizate:  # autorizate() == login and
        name = 'Slavik'  # input("Input User name: ")
        surname = 'ok_SYS'  # input("Input User surname: ")
        login = 'Lex'  # input("Input User login: ")
        password = '444'  # input("Input User password: ")
        user_rights = 'admin'  # input("Input User rights: (admin / user / guest): ")
        mail = 'sayt@3g.ua'  # input("Input User mail: ")
        status = False
        print(time_string, datum)
        try:
            new_user = Users(name, surname, login, password, user_rights, mail, time_string, datum, status)
            users.append(new_user)
            if new_user:
                print(f"User {new_user.name},{new_user.login} created!")
            else:
                raise ValueError
        except ValueError:
            print("Something is wrong!")
            # new_user = user_add()


def transaction(user):
    print(user)
    usero = user.__getattribute__('user_rights')
    user_rights = user.get_user_rights()
    print(usero, user_rights)
    if user_rights == 'admin':
        print('admin')
    elif user_rights == 'user':
        print('user')
    elif user_rights == 'superuser':
        print('superuser')


# Сделать функцию ассинхронной
def user_status():
    while True:
        for user in users:
            if user.status_getter():
                print("Ожидаем выход из онлайна: ")
                sleep(3)
                user.status_setter(False)  # Перезаписывать время последнего онлайна с переодичностью
                users.remove(user)
                print('User log-off', users)
                return users
            else:
                user.status_setter(True)

if __name__ == '__main__':
    main()
