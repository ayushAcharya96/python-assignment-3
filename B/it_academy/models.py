
class Course:
    # count = 1
    def __init__(self, name):
        # self.id = count
        self.name = name
        self.duration = '12 Weeks'
        self.price = 20000
        # count++
    def __str__(self):
        return'{}\t{}\t{}'.format(self.name, self.duration, self.price)


class Student:
    def __init__(self, name, college_name, deposits, course, status='ENROLLED'):
        self.name = name
        self.college_name = college_name
        self.deposits = deposits
        self.course = course
        self.course_status = 'ENROLLED'
        self.first_installment = 'Paid'
        self.second_installment = 'Paid'
        if deposits == '10000':
            self.first_installment = 'Paid'
            self.second_installment = 'Not Paid'

    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}'.format(self.name, self.college_name, self.course, self.course_status, self.first_installment, self.second_installment)
        