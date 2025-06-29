#with for loop we can execute a set of statements.
#print each fruit in a fruit list
fruits =[ "apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
#looping through string
for x in "banana":
    print(x)
    
fruits= ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break # we can stop the loop before it loop all the items
    
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
      if x == "banana":
        break # break before print can exit the loop
      print(x)
      
#continue statement:stop current iteration and continue next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
      if x == "apple":
       continue
      print(x)
for x in range(5): #range function return a sequence of number from 0 and incremnet by 1
    print(x)

fruits = ["apple", " banana", "cherry"] 
for x in fruits:
    if x == "banana":
        continue
    print(x)
for x in range(2,30 ,3): #increment the sequence with 3
    print(x)  

#Else in for loop
#(used to specify a block of code to be executed when the loop is finished)
for x in range(6):
    print(x)
else:
    print("Finally finished")

#example:
#break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x ==3:
        break
    print(x)
else:
    print("finally finished")