from lab11_library.model.book import Book
from lab11_library.model.reader import Reader


def return_book(book_id):
    book = Book.get_book(book_id)
    if book is None:
        return "Book doesnt exist!" # czy to nie powinien być wyjątek?
    elif book.loaned_to is None:
        return "Book is not loaned!"
    else:
        book.return_book()
        return 'Book returned successfully'


def add_book(title, author, publication_date):
    book = Book(title, author, publication_date)
    book.add_to_database()
    return 'Book added successfully'


def delete_book(user, book_id):
    book = Book.get_book(book_id)
    if book is None:
        return "Book doesnt exist!"
    elif book.loaned_to is not None:
        return "Book cannot be deleted while loaned!"
    else:
        book.remove_from_database()
        return 'Book deleted successfully'


def add_reader(login, first_name, last_name):
    if Reader.get_reader(login) is not None:
        return 'Reader already exists!'
    else:
        reader = Reader(first_name, last_name, login)
        reader.add_to_database()
        return 'Reader added successfully'


def main_loop_employee(user):
    while True:
        print('See catalog - type 1\nReceive return - type 2\nAdd book - type 3\nDelete book - type 4\nAdd reader - '
              'type 5\nExit - type 6')
        command = input()
        if command == '1':
            for book in Book.get_all_books():
                print(book)
            print()
        elif command == '2':
            print('Provide id of the returned book:')
            # try:
            book_id = int(input())
            print(return_book(book_id))
            # except ValueError:
            #     print('Wrong id format!')
            print()
        elif command == '3':
            print('Provide info the book you want to add in the format: title,author,publication_date')
            try:
                title, author, publication_date = input().split(',')
                publication_date = int(publication_date)
                print(add_book(title, author, publication_date))
            except ValueError:
                print('Wrong data format!')
            print()
        elif command == '4':
            print('Provide id of the book you want to delete:')
            try:
                book_id = int(input())
                print(delete_book(user, book_id))
            except ValueError:
                print('Wrong id format!')
            print()
        elif command == '5':
            print('Provide user info in the format: login,first_name,last_name')
            try:
                login, first_name, last_name = input().split(',')
                print(add_reader(login, first_name, last_name))
            except ValueError:
                print('Wrong data format!')
            print()
        elif command == '6':
            break
        else:
            print('Unknown command!')
