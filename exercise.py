#Write a function to calculate the square of numbers
def square(num):
    return num ** 2

print(square(5)) 

#Write a function that returns the maximum of 3 numbers.
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three(12, 25, 9))  

#Create a function that returns the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  

#Write a function that checks whether a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11)) 
print(is_prime(10))

#Simple calculator fucntion
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation"

print(calculator(10, 5, "add"))       
print(calculator(10, 5, "subtract"))  
print(calculator(10, 5, "multiply"))  
print(calculator(10, 5, "divide")) 

   
#Calculate the factorial of a number using a loop
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "is", fact)

#check if the number is prime 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  
print(is_prime(10))  

# reverse a string
text = "Ashma"
reversed_text = text[::-1]
print(reversed_text)  

#list of dictionaries to a file (as CSV)

import csv
data = [
    {"name": "Ashma", "age": 20},
    {"name": "Sam", "age": 22}
]
with open("people.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)


