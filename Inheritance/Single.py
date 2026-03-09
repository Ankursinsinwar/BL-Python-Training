'''
Single Inheritance
'''

class Person:
    def show_name(self):
        print("Name: Ankur")

class Student(Person):
    def show_course(self):
        print("Course: Computer Science")

s = Student()

s.show_name()
s.show_course()