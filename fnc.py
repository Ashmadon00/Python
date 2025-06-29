def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
    
def isGreater(a, b):
    if(a>b):
     print("First number is greater")
    else:
     print("Second number is greater or equal")

def isLesser(a,b): 
    pass   
    
    
a = 9
b = 8
isGreater(a, b)
calculateGmean(a,b)
#gmean = (a*b)/(a+b)
#print(gmean)

c = 3
d = 4
isGreater(c, d)
calculateGmean(c,d)
#gmean2 = (c*d)/(c+d)
#print(gmean2)

def greet(): #all the code inside function is executed.
    print("Hello World!")
#call the function
greet()#greet function is called, the program's control transfer to the function definition.
print("Outside function")#control of the program jumps to the next statemnet after the function call.

#DEFAULT parameter value
def my_function(country ="Norway"):
    print("I am from"+ country)
my_function("Sweden")
my_function("india")
my_function() # without argument it uses deafult value
my_function("china")

#passing a list as an argument
def my_function(food):
    for x in food:
        print(x)
fruits =  ["apple", "banana", "cherry"]
my_function(fruits)

#Return values
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(8))
print(my_function(6))

def my_function(x, /): #to specify that a function can have only positional arguments.
    print(x)
my_function(3)

def my_function(x):#without,/ we are allowed to use keyword arguments even if the function expects positonal arguments
    print(x)
my_function(x = 3)

