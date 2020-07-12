from .models import Course, Student
# from .utils import validate_student, validate_course

class CourseView:
    course_dict = {}

    def get_course_data_from_user(self):
        course_name = input('Enter course name : ').strip()
        return Course(course_name)
    
    def create_course(self):
        course = self.get_course_data_from_user()
        if self.validate_course(course):
            CourseView.course_dict[course.name.lower()] = course

    def display_courses(self):
        print('\t<<<<******    Courses Offered    ******>>>>')
        for course in CourseView.course_dict.values():
            print(f'\t{str(course)}')

    def validate_course(self, course):
        if course.name == '':
            print('Course name cannot be empty')
        elif course.name in CourseView.course_dict.keys():
            print('Course already exists')
        else:
            print('Registering course...')
            return True


class StudentView:
    student_dict = {}

    def get_student_info_from_user(self):
        name = input('Enter your full name : ').strip()
        college_name = input('Enter your college name : ').strip()
        deposits = input('Enter your deposite amount : ').strip()
        course = input('Enter the course you are interesed in : ').strip()
        return Student(name, college_name, deposits, course)

    def register(self):
        student = self.get_student_info_from_user()
        if self.validate_student(student):
            if self.student_exists(student):
                print('Student already exists.')
            else:
                StudentView.student_dict[(student.name.lower(), student.college_name.lower())] = student
    
    def update(self):
        if self.delete():
            self.register()
    
    def delete(self):
        name = input('Enter name : ').strip()
        college = input('Enter college name : ').strip()
        if (name.lower(), college.lower()) in StudentView.student_dict.keys():
            del StudentView.student_dict[(name.lower(),college.lower())]
            return True
        print('Student doesnot exist')
        return False
    
    def complete_course(self):
        name = input('Enter name : ').strip()
        college = input('Enter college name : ').strip()
        if (name.lower(), college.lower()) in StudentView.student_dict.keys():
            if StudentView.student_dict[(name.lower(), college.lower())].deposits == '20000':
                StudentView.student_dict[(name.lower(), college.lower())].course_status = 'COMPLETED'
                StudentView.student_dict[(name.lower(), college.lower())].deposits = 0
            else:
                print('You have payment dues. Complete your payment first.')
                return False
            return True
        print('Student doesnot exist')
        return False


    def display_student(self):
        print('\t<<<<******    Students Registered    ******>>>>\n')
        # print('\nName\tCollege Name\tCourse\tCompleted\tFirst Installment\tSecond Installment')
        for student in StudentView.student_dict.values():
            print(f'{str(student)}')
    

    def validate_student(self, student):
        if student.name == '' or \
            student.college_name == '' or \
                    student.course == '':
            print('All fields are required')
        elif student.course.lower() not in CourseView.course_dict.keys():
            print('Enter Valid Course')
        elif student.first_installment == 'Not Paid':
            print('Deposit must be Rs.10000 or Rs.20000')
        else:
            print('Registering Student....')
            return True
    def student_exists(self, student):
        if (student.name.lower(), student.college_name.lower()) in StudentView.student_dict.keys():
            return True