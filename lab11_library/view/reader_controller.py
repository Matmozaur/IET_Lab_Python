from lab11_library.model.book import Book


def loan_book(user, book_id):
    book = Book.get_book(book_id)
    if book is None:
        return "Book doesnt exist!"
    elif not book.available:
        return "Book cannot be loaned!"
    else:
        book.loan(user)
        return 'Book loaned successfully'


def main_loop_reader(user):
    while True:
        print('See catalog - type 1\nLoan book - type 2\nExit - type 3')
        command = input()   # DRY
        if command == '1':
            for book in Book.get_all_books():
                print(book)
            print()
        elif command == '2':
            print('Provide id of the book you want to loan:')
            try:
                book_id = int(input())
                print(loan_book(user, book_id))
            except ValueError:
                print('Wrong id format!')
            print()
        elif command == '3':
            break
        else:
            print('Unknown command!')
