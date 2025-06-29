#Inheritance allows us to define a class that inherits all the methods and properties from another class.

#create classs
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
x = Person("Ashma", "Shahi")
x.printname()
class Student(Person): # create a class
    pass
x = Student("Radha", "Shyam")
x.printname()
#_init_() function is called automatically every time the class is being used to create a new object.
#(instead of pass)
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Ashu", "Baby")
x.printname()
    
class Student(Person):
 def __init__(self, fname, lname):
     super().__init__(fname, lname)

#example
#Add a property called graduationyear to the student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Ashma", "Shahi", 2084)
print(x.graduationyear)

#Add a method called Welcome to the student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    
def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of",  self.graduationyear)
x = Student("Ashma", "Shahi", 2084)
print(x.graduationyear)
 #If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.   