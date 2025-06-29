#Creating a module
def greeting(name):
  print("Hello, " + name)
  #using mode import
import mymodule

mymodule.greeting("Ashma")
#Variables in Module
person1 = {
  "name": "Sita",
  "age": 33,
  "country": "Nepal"
}
import mymodule

a = mymodule.person1["age"]
print(a)

#Re-naming a Module using as keywords
import mymodule as mx
a = mx.person1["age"]
print(a)
#Built-in Modules
import platform
x = platform.system()
print(x)

#using dir() function: built in function to list function / variable name 
import platform

x = dir(platform) #can be used on all modules
print(x)

#import from module
def greeting(name):
    print("Hello," + name)
person1 = {
    "name" : "Radha",
    "age" : 22,
    "Country": "India"
}
from mymodule import person1
print (person1["age"])