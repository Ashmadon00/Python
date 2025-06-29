#its items are ordered, changeable and do not allow duplicates.
thisdict = {
  "name": "Ram",
  "age": "20",
  "address": "Nepal"
}
print(thisdict["age"])
print(len(thisdict))#length

thisdict = {
  "name": "Ram",
  "age": "20",
  "address": "Nepal"
}
print(type(thisdict))
#using dict() method to make a dictionary:
thisdict = dict(name = "Ram", age = 16, country = "Nepal")
print(thisdict)

thisdict =	{
  "name": "Ashma",
  "age": "22",
  "year": 2025
}
x = thisdict["year"]#value of modelkey
print(x)
x = thisdict.get("name")
print(x)

#add a new item to the original dictionary and see that the keys list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) 