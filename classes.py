from authorization import registration


class Users:
    def __init__(self, name, surname, login, password, user_rights, mail, time_string, datum, status):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.user_rights = user_rights
        self.mail = mail
        self.time_string = time_string
        self.datum = datum
        self.status = status

    def as_dict(self):
        return {'name': self.name, 'surname': self.surname, 'login': self.login, 'password': self.password,
                'user_rights': self.user_rights, 'mail': self.mail, 'time_string': self.time_string,
                'self.datum': self.datum, 'self.status': self.status}

    def add_user(self):
        print("Передача обьекта на запись!")
        try:
            registration(self.as_dict())
        # except TypeError:
        #     print('Не удалось записать нового пользователя, обратитесь в поддержку.')
        except Exception:
            print('Ошибка записи - файл БД отсутствует.')
        else:
            print("False")

    def status_setter(self, status):
        self.status = status

    def status_getter(self):
        return self.status

    def get_user_rights(self):
        return self.user_rights

class Transaction:
    def __init__(self, ):
        pass