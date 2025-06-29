#Create class
class MyClass :
    x= 5
print(MyClass)

#create object
p1 = MyClass()
print(p1.x)
#a function called __init__(), which is always executed when the class is being initiated.
#Use to assign values to object properties, or other operations that are necessary to do when the object is being created
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ashma", 36)

print(p1.name)
print(p1.age)
#The __str__() function controls what should be returned when the class object is represented as a string.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ashma", 36)

print(p1)
#example:The string representation of an object WITH the __str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Ashma", 36)

print(p1)