#syntax input() function allows user input
x = input('Enter your name:')
print('Hello,' + x)
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
 #print() for printing output
# Single variable
s = "Bob"
print(s)

# Multiple Variables
s = "Alice"
age = 25
city = "New York"
print(s, age, city)

# multiple input
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

#conditional input
# Prompting the user for input
age_input = input("Enter your age: ") # Converting the input to an integer
age = int(age_input) # Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    
#printing numbers
# Taking input as int
# Typecasting to int
n = int(input("How many roses?: "))
print(n)
price = float(input("Price of each rose?: ")) #float input
print(price)

#datatypes of input
a = "Hello World"
b = 10
c = 11.22
d = ("Apple", "Banana", "Cherry")
e = ["Apple", "Banana", "orange"]
f = {"Apple": 1, "Banana":2, "Orange":3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))