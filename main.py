
from authorization import autorizate
from classes import Users

def main():
    autorizate()

def user_add():
    login = 'Lex'
    User_Autorizate = True
    if User_Autorizate: #autorizate() == login and
        name = 'Slavik' #input("Input User name: ")
        surname = 'ok_SYS' #input("Input User surname: ")
        login = 'OK_sys' #input("Input User login: ")
        password = '777' #input("Input User password: ")
        user_rights = 'admin' #input("Input User rights: (admin / user / guest): ")
        mail = 'sayt@3g.ua' #input("Input User mail: ")
        try:
            new_user = Users(name, surname, login, password, user_rights, mail)
            if new_user:
                print(f"User {new_user.name},{new_user.login} created!")
            else:
                raise ValueError
        except ValueError:
            print("Something is wrong!")
            new_user = user_add()





if __name__ == '__main__':
    main()
    user_add()
