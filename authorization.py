# from Exceptions import AutorizationError

def getUser(login, password):
    global message
    with open('DataBase/db.csv', 'r') as f:
        log = False
        for line in f:
            arr = line.strip().replace(':', ',').replace('{', '').replace("}", "").replace('"', '').replace("'", "").split(',')
            for value in arr:
                if value.replace(' ', '') == str(login):
                    log = True
                if password == value.replace(' ', '') and log:
                    message = 'Добро пожаловать,'
                    return True
        if log and password not in arr:
            message = f'Неверный пароль'
            return False

        message = f'Пользователь {login} не найден'
        return False


# def getUser(login, password):
#     global message
#     with open('DataBase/db.csv', 'r') as f:
#         for line in f:
#             arr = line.strip().split(':')
#             if login in arr and password in arr:
#                 message = 'Добро пожаловать,'
#                 return True
#             if login in arr:
#                 message = f'Неверный пароль'
#                 return False
#
#         message = f'Пользователь {login} не найден'
#         return False
#

def autorizate():
    while True:
        login = 'Lex' #input('Введите логин:')
        password = '444' #input('Введите пароль:')
        if getUser(login, password):
            print(f'{message} {login}')
            return login
        else:
            print(message)


def registration(reg_data):
    user_data = []
    for i, j in zip(list(reg_data.keys()), list(reg_data.values())):
        user_data.append(f'{i}: {j}')
        if i == 'login' and userExist(j):
            print(f"{i}: {j}, {userExist(j)}")
    with open("DataBase\db.csv", 'a') as f:
        f.write(f'{user_data}' + '\n')
        # f.write(reg_data.name + ':' + reg_data.surname + ':' + reg_data.login + ':' + reg_data.password +
        # ':' + reg_data.user_rights + ':' + reg_data.mail + '\n')
    # return user_data



def userExist(login):
    with open('DataBase/db.csv', 'r') as f:
        for line in f:
            arr = line.strip().split(':')
            # print(login)
            if login in arr:
                return True
    return False


message = ''
