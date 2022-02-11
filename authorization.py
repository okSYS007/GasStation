#from Exceptions import AutorizationError

def getUser(login, password):
    global message
    with open('DataBase/db.csv') as f:
        for line in f:
            arr = line.strip().split(':')
            if login in arr and password in arr:
                message = 'Добро пожаловать,'
                return True    
            if login in arr:
                message = f'Неверный пароль'
                return False
            
        message = f'Пользователь {login} не найден'
        return False
    
def autorizate():
    user_autorizate = False
    while True:
        login = input('Введите логин:')
        password = input('Введите пароль:')
        if getUser(login, password):
            print(f'{message} {login}')
            user_autorizate = True
            break
        else:
            print(message)

    return user_autorizate

    
                
message = ''