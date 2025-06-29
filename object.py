#Objects can also contain methods. Methods in objects are functions that belong to the object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
print(p1.age)
p1.myfunc()
#The self parameter is a reference to the current instance of the class
#use the words mysillyobject and abc instead of self
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#modify object properties
#set the age of p1 to 40
p1.age = 40
#delete object properties
del p1.age
#delete objects
del p1
