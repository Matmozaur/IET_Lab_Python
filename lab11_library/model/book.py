import json
import os

from lab11_library.model.reader import Reader

script_dir = os.path.dirname(__file__)


def communicate_database(func):
    def wrap(*args, **kwargs):
        with open(os.path.join(script_dir, 'books.json')) as books:
            data = json.load(books)
        result = func(*args, **kwargs, data=data)
        with open(os.path.join(script_dir, 'books.json'), 'w') as books:
            json.dump(data, books, indent=4)
        return result
    return wrap


def read_database(func):
    def wrap(*args, **kwargs):
        with open(os.path.join(script_dir, 'books.json')) as books:
            data = json.load(books)
        result = func(*args, **kwargs, data=data)
        return result
    return wrap


class Book:

    def __init__(self, title, author, release, available=True, loaned_to=None, book_id=None):
        self.title = title
        self.author = author
        self.release = release
        self.available = available
        self.loaned_to = loaned_to
        self.book_id = book_id

    def __str__(self):
        return 'Id: ' + str(self.book_id) + ', "' + self.title + '", ' + self.author + ', ' + str(self.release) + \
               (', available' if self.available else '')

    @communicate_database
    def add_to_database(self, data=None):
        data['Last id'] += 1
        self.book_id = data['Last id']
        data['Books'][self.book_id] = {
            "Title": self.title,
            "Author": self.author,
            "Release": self.release,
            "Available": self.available,
            "Loaned to": self.loaned_to
        }

    @communicate_database
    def remove_from_database(self, data=None):
        del data['Books'][str(self.book_id)]

    @staticmethod
    @read_database
    def get_all_books(data=None):
        result = []
        for book_id in data['Books'].keys():
            result.append(Book(data['Books'][book_id]['Title'], data['Books'][book_id]['Author'],
                               data['Books'][book_id]['Release'], data['Books'][book_id]['Available'],
                               data['Books'][book_id]['Loaned to'], int(book_id)))
        return result

    @staticmethod
    @read_database
    def get_book(book_id, data=None):
        for idb in data['Books'].keys():
            if int(idb) == book_id:
                return Book(data['Books'][idb]['Title'], data['Books'][idb]['Author'],
                            data['Books'][idb]['Release'], data['Books'][idb]['Available'],
                            data['Books'][idb]['Loaned to'], int(book_id))
        return None

    @communicate_database
    def loan(self, reader, data):
        reader.loan(self)
        data['Books'][str(self.book_id)]['Available'] = False
        data['Books'][str(self.book_id)]['Loaned to'] = reader.login

    @communicate_database
    def return_book(self, data=None):
        data['Books'][str(self.book_id)]['Available'] = True
        Reader.get_reader(data['Books'][str(self.book_id)]['Loaned to']).return_book(self)
        data['Books'][str(self.book_id)]['Loaned to'] = None


if __name__ == '__main__':
    # x = Book('Blood of Elves', 'Andrzej Sapkowski', 2009)
    # x.add_to_database()
    for book in Book.get_all_books():
        print(book)

