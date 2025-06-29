#if statement using 'if' keyword
a = 88
b = 200
if a == b:
 print("b is equal to a")
 # if i do this there will be indentation error so right way is:
x = 88
y = 400
if y > x:
    print("y is greater than x")
elif x == y: #we introduce ifelse(elif)
    print("x and y are equal") 
else:
    print("x is greater than y ")

a = 3
b = 333
print("A") if a > b else print("B") #one line ifelse statement
#also known as ternary operators or conditional expressions.

# one line if else statement with 3 conditions
a = 330
b = 300
print("A") if a > b else print("=") if a == b else print("B")
 
#Add and Or, Not
a = 200
b = 99
c = 600
if a > b and c > a:
    print("Both conditions are true")
if a > b or a > c: 
    print("At least one of the conditions is True")
if not a < b:
    print("a is NOT less than b")

#Nested if(if inside if)
x = 33
if x > 20:
    print("Above 20,")
    if x > 10:
        print("and also above 10!")
    else: 
        print("but not above 20.")
        
#pass statement
#if statemnet with no content then put pass to avoid error
a = 22
b = 200
if b > a:
     pass