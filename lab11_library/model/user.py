class User:

    def __init__(self, first_name, last_name, login):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', login: ' + self.login
