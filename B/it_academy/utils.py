
import csv
from .views import StudentView, CourseView
from .models import Course, Student

STUDENT_FILE = 'students.csv'
COURSE_FILE = 'course.csv'

def save_data_csv():
    with open(STUDENT_FILE, mode='w') as student_data:
        student_writer = csv.writer(student_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow(['name', 'college_name', 'deposit', 'course','status'])
        for student in StudentView.student_dict.values():
            s = (student.name, student.college_name, student.deposits, student.course, student.course_status)
            student_writer.writerow(s)
    with open(COURSE_FILE, mode='w') as course_data:
        course_writer = csv.writer(course_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        course_writer.writerow(['name', 'duration', 'price'])
        for course in CourseView.course_dict.values():
            c = (course.name, course.duration, course.price)
            course_writer.writerow(c)

def load_data_csv():
    with open(COURSE_FILE, mode='r') as course_data:
        course_reader = csv.DictReader(course_data)
        for row in course_reader:
            course = Course(row['name'])
            print(str(course))
            CourseView.course_dict[course.name.lower()] = course
    with open(STUDENT_FILE, mode='r') as student_data:
        student_reader = csv.DictReader(student_data)
        for row in student_reader:
            student = Student(row['name'], row['college_name'], row['deposit'], row['course'], row['status'])
            StudentView.student_dict[(student.name.lower(), student.college_name.lower())] = student