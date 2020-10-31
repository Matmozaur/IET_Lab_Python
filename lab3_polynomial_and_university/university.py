from datetime import datetime


class Person:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.inbox = dict()

    def send_email(self, author, message):
        self.inbox[(author, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))] = message
        print("Email with the following content: \"{}\" has been sent to email address \"{}\".".format(message,
                                                                                                       self.email))

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email


class Worker(Person):

    def __init__(self, first_name, last_name, email, room):
        Person.__init__(self, first_name, last_name, email)
        self.room = room

    def __str__(self):
        return Person.__str__(self) + ' ' + self.room


class TeachingWorker(Worker):

    def __init__(self, first_name, last_name, email, room, subjects, consultation):
        Worker.__init__(self, first_name, last_name, email, room)
        self.subjects = subjects
        self.consultation = consultation

    def __str__(self):
        return Worker.__str__(self) + ' ' + str(self.subjects) + ' ' + self.consultation


class ResearchWorker(Worker):

    def __init__(self, first_name, last_name, email, room, publications):
        Worker.__init__(self, first_name, last_name, email, room)
        self.publications = publications

    def add_publications(self, publication):
        self.publications.append(publication)

    def __str__(self):
        return Worker.__str__(self) + ' ' + str(self.publications)


class ResearchTeachingWorker(ResearchWorker, TeachingWorker):

    def __init__(self, first_name, last_name, email, room, publications, subjects, consultation):
        ResearchWorker.__init__(self, first_name, last_name, email, room, publications)
        TeachingWorker.__init__(self, first_name, last_name, email, room, subjects, consultation)

    def __str__(self):
        return TeachingWorker.__str__(self) + ' ' + str(self.publications)


class Student(Person):

    def __init__(self, first_name, last_name, email, index, grades=None):
        Person.__init__(self, first_name, last_name, email)
        self.index = index
        if grades is None:
            self.grades = {'default_subject1': [], 'default_subject2': []}
        else:
            self.grades = grades

    def add_grade(self, subject, grade):
        try:
            self.grades[subject].append(grade)
        except KeyError:
            print('Student is not enrolled on ' + subject)

    def __str__(self):
        return Person.__str__(self) + ' ' + str(self.index) + ' ' + str(self.grades)


if __name__ == "__main__":
    student = Student('X', 'Y', 'a@b', 222222)
    print(student)
    tw = TeachingWorker('X', 'Y', 'a@b', '17a', ['subject_1', 'subject_2'], 'Monday 17:00')
    print(tw)
    rw = ResearchWorker('X', 'Y', 'a@b', '15b', ['pub_1', 'pub_2'])
    print(rw)
    rtw = ResearchTeachingWorker('X', 'Y', 'a@b', '15a', ['subject_1', 'subject_2'], ['pub_1', 'pub_2'], 'Monday 17:00')
    print(rtw)
    rtw.send_email('student1', 'Best regards')
    print(rtw.inbox)
