'''
Hybrid Inheritence
'''


class Person:
    def show_person(self):
        print("I am a person")

class Employee(Person):
    def show_employee(self):
        print("I am an employee")

class Student(Person):
    def show_student(self):
        print("I am a student")

class Intern(Employee, Student):
    def show_intern(self):
        print("I am an intern")

i = Intern()

i.show_person()
i.show_employee()
i.show_student()
i.show_intern()