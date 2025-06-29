#while loops
#we can execute a set of statements as long as condition is true
i = 1
while i < 6:
    print(i)
    i += 1
#break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break # with break we cans top the loop even if while condition is true
    i += 1
    
#continue statement
i = 0
while i < 6:
    i += 1
    if i ==3: #if i = 3 then continue
        #output will be 1 2 4 5 6
        continue
    print(i)

#else statement
#we can run a block of code once when the condition no longer is true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")