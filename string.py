#surrounded by either single quotation marks or double quotation marks
print("Hello there")
print("Hello Worlds")
print('How are you doing')

# assign string to a variable
a = "apple"
print(a)
#for multiline string use three quotes
b = """" Hello, How are you?, Its rainy today, Quite chill day, Im good. Have you had your dinner?"""
print(b)
# strings are arrays
#strings in python are arrays of bytes representing unicode characters.
a = "Hello, World!" #first character has position 0 
print(a[1])
#loop
for x in "Banana":
    print(x)
    
#string length
a = "Hello, World!"
print(len(a))
#check string
txt = "The best thing in life are free!" #to check certain pharse or character is present in a string, we use in keyword
print("free" in txt) # there is free keyword present there so output is true
#use if
txt = "The best things in life are free"
if "free" in txt:
    print("Yes", 'free is present')

#not in(not present)
txt = "The best things in life are free!"
print("expensive" not in txt)

#example
#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No,'expensive' is NOT present.")
#slicing
#we can return a range of characters by using the slice syntax
b = "Hell0 Ashma"
print(b[:4]) #start
print(b[2:]) #end
print(b[-4: -3]) #negative indexing

#modifying
#upper case( returns the string in upper case)
a = "Hello, World!"
print(a.upper())
print(a.lower()) #lower case
print(a.strip()) #remove any whitespace
print(a.replace("H", "j")) #replace string
print(a.split(",")) #split to split the string into sub strings 

#String concatenation
#to concatenate, or combine, two strings you can use the + operator
#example: Merge variavle a with variable b into variable c
a = "Hello"
b = " World"
c = a +b
print(c)
d = a + " " + b
print(d) #add space

#string format
#age = 34
#txt = " My name is Ashma" +age #we cannot combine string and numbers 
#print(txt)
#to combine we use f-string format()
age = 22
txt = f"My name is Ram. I am {age}"
print(txt)

#placeholders  contain variables, operations, functions and modifiers to format value
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 20
txt = f"The price is {price:.2f} dollars" #.2f means fixed point numbers with 2 decimal
print(txt)

#perform a math operation in the placeholder, and return the result
txt = f"The price is {20*59} dollars"
print(txt)