import json
import os
from lab11_library.model.user import User

script_dir = os.path.dirname(__file__)


def communicate_database(func):
    def wrap(*args, **kwargs):
        with open(os.path.join(script_dir, 'readers.json')) as readers:
            data = json.load(readers)
        result = func(*args, **kwargs, data=data)
        with open(os.path.join(script_dir, 'readers.json'), 'w') as readers:
            json.dump(data, readers, indent=4)
        return result
    return wrap


def read_database(func):
    def wrap(*args, **kwargs):
        with open(os.path.join(script_dir, 'readers.json')) as readers:
            data = json.load(readers)
        result = func(*args, **kwargs, data=data)
        return result
    return wrap


class Reader(User):

    def __init__(self, first_name, last_name, login, loaned=None):
        User.__init__(self, first_name, last_name, login)
        if loaned is None:
            loaned = []
        self.loaned = loaned

    @communicate_database
    def add_to_database(self, data):
        data[self.login] = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'loaned': []
        }

    @staticmethod
    @read_database
    def get_reader(login, data=None):
        user_data = data.get(login, None)
        if user_data is None:
            return None
        return Reader(login=login, **user_data)

    @communicate_database
    def loan(self, book, data):
        data[self.login]['loaned'].append(book.book_id)

    @communicate_database
    def return_book(self, book, data=None):
        data[self.login]['loaned'].remove(book.book_id)
