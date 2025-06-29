#function only runs when it is called
#it can return data as return

#create a function(using def)
def my_function():
    print("Hello World!")
my_function() # calling function

#arguments(seperate with comma add  arguments as many as you )
def my_function(fname):#function name
    print(fname + "Ashma")
my_function("Email:")
my_function("DOB:")
my_function("Address:")

#number of arguments
def my_function(fname, lname):
    print(fname + "" + lname)
my_function("Email", "Ashma")
#arbitrary arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("css", "java", "php")

def my_function(child3, child2, child1): #key words arguments
  print("The youngest child is " + child3)

my_function(child1 = "Cs", child2 = "OS", child3 = "CN")
#if the number of keyword arguments is unknown, add ** before parameter
def my_function(**kid):
  print("The youngest child is " + kid["lname"])

my_function(fname = "Ram", lname= "sita")
