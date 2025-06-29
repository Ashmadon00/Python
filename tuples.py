#tuples are used to store multiple items in a single variables.
#create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)# this allows duplicates also

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))# tuples length len()

#creating tuple with one item
thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple") #without comma its not a tuple
print(type(thistuple))
#tuple items can be of any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(type(tuple2))