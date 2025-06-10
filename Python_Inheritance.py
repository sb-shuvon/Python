class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2023

x = Student("Mike", "Olsen")
print(x.graduationyear)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2023)
x.welcome()
