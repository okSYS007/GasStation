
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
            else:
                message = f'Пользователь {login} не найден'
                return False
    
def autorizate():
   
    while True:
        login = input('Введите логин:')
        password = input('Введите пароль:')
        if getUser(login, password):
            print(f'{message} {login}')
            break
        else:
            print(message)
                
message = ''
