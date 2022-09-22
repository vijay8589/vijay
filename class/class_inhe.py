"""class method works for the inheritance"""

import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, datetime.date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, datetime.date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('vijay', 1997)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('venkateswarlu',1970 ,20)
print(isinstance(man1, Man))
