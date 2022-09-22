# using class method

class vijay:
    course = 'msc'

    def purchase(obj):
        print("Puchase course : ", obj.course)


vijay.purchase = classmethod(vijay.purchase)
vijay.purchase()


"""Create class method using classmethod()"""


class Student:
    # create a variable
    name = "vijay"

    # create a function
    def print_name(obj):
        print("The name is : ", obj.name)


# create print_name classmethod

Student.print_name = classmethod(Student.print_name)

# print_name() method is called a class method
Student.print_name()

"""Factory method using Class method"""

import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, datetime.date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)


person = Person('vijay', 25)
person.display()