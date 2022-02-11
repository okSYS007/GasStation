
from authorization import userExist

def registration(reg_data):
    
    for user_login, user_password in reg_data.items():
        if not userExist(user_login):
            with open("DataBase\db.csv", 'a') as f:
                f.write(user_login + ':' + user_password)

reg_data = {'Slava123': '123'}
registration(reg_data)