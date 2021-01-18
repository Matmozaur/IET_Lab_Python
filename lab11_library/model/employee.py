import json
import os

from lab11_library.model.user import User

script_dir = os.path.dirname(__file__)


def communicate_database(func): # deja vu + nie używane
    def wrap(*args, **kwargs):
        with open(os.path.join(script_dir, 'employees.json')) as employees:
            data = json.load(employees)
        result = func(*args, **kwargs, data=data)
        with open(os.path.join(script_dir, 'employees.json'), 'w') as employees:
            json.dump(data, employees, indent=4)
        return result
    return wrap


def read_database(func):
    def wrap(*args, **kwargs):
        with open(os.path.join(script_dir, 'employees.json')) as employees:
            data = json.load(employees)
        result = func(*args, **kwargs, data=data)
        return result
    return wrap


class Employee(User):

    @staticmethod
    @read_database
    def get_employee(login, data=None):
        user_data = data.get(login, None)
        if user_data is None:
            return None
        return Employee(login=login, **user_data)
