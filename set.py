#set are used to store multiple items in a single variable
thisset = {"apple", "banana", "cherry"} #create set
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
#true and 1 is considered the same value
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #we use len() to get the length
#data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

myset = {"apple", "banana", "cherry"}
print(type(myset))#data type of particular set
#we can aslo use set() double round bracket to make a set
thisset = set(("apple", "banana", "cherry"))
print(thisset)