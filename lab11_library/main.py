from model.employee import Employee
from model.reader import Reader
from view.employe_controller import main_loop_employee
from view.reader_controller import main_loop_reader


def get_user(login):
    reader = Reader.get_reader(login)
    if reader is not None:
        return reader, 'reader' # czy rola nie powinna być częścią obiektu user?
    employee = Employee.get_employee(login)
    if employee is not None:
        return employee, 'employee'
    return None, None


def run():  # zwyczajowo main()
    while True: # sugeruję skrócić tego while'a tylko do walidacji użytkownika
        print("Provide login:")
        login = input()
        user, user_type = get_user(login)
        if user is not None:
            if user_type == 'reader':
                main_loop_reader(user)
            if user_type == 'employee':
                main_loop_employee(user)
            break


if __name__ == '__main__':
    run()
