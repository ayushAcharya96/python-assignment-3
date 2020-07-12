from .views import CourseView, StudentView
from .models import Course, Student
from .utils import save_data_csv, load_data_csv

class App:

    def __init__(self):
        self. cv = CourseView()
        self.sv = StudentView()
    
    def start(self):
        load_data_csv()
        while(True):
            self.show_menu()
            choice = input('=>')
            if choice == '1':
                self.add_course()
            elif choice == '2':
                self.inquiry_course()
            elif choice == '3':
                self.register_for_course()
            elif choice == '4':
                self.display_student_info()
            elif choice == '5':
                self.update_student_info()
            elif choice == '6':
                self.delete_student_info()
            elif choice == '7':
                self.graduate_student()
            elif choice == 'e' or choice == 'E':
                print('Exiting from the system.....')
                break
            else:
                print("Invalid input please select valid choice.")
            input()
        save_data_csv()
    
    def add_course(self):
        self.cv.create_course()

    def inquiry_course(self):
        self.cv.display_courses()

    def register_for_course(self):
        self.sv.register()

    def display_student_info(self):
        self.sv.display_student()

    def update_student_info(self):
        self.sv.update()

    def delete_student_info(self):
        self.sv.delete()

    def graduate_student(self):
        self.sv.complete_course()

    def show_menu(self):
        print('\n\n<<<<*****   INSIGHT ACADEMY    ****>>>>')
        print('\nWhat do you want to do?\n')
        print('\t1   -->  Add a course')
        print('\t2   -->  Inquiry about courses')
        print('\t3   -->  Register for a course')
        print('\t4   -->  Display Student Information')
        print('\t5   -->  Update Student Information')
        print('\t6   -->  Delete Student Information')
        print('\t7   -->  Graduate a Student')
        print('\te/E -->  Exit')

app = App()
app.start()