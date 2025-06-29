#Create a Hash Function that sums the Unicode numbers of each character and return a number between 0 and 9:

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

print("'Ram' eats Rice:", hash_function('Ram'))

 #Inserting an Element
my_list = [None, None, None, None, None, None, None, None, None, None]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def add(name):
  index = hash_function(name)
  my_list[index] = name
  
def contains(name):
  index = hash_function(name) #looking up a name
  return my_list[index] == name

add('Ram')
add('Bob')
add('Puntu')
add('Jerry')
add('sita')
add('kaju')
print(my_list)
print("'Jerry' is in the Hash Table:", contains('Pete'))

#handling collisions
my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def add(name):
  index = hash_function(name)
  my_list[index].append(name)

def contains(name):
  index = hash_function(name)
  return my_list[index] == name

add('Apple')
add('Banana')
add('Orange')
add('Cherry')
add('Carrot')
add('Pear')
print(my_list)