#Error handling
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
    
    
try:
  print("Hello")
except: 
  print("Something went wrong")
else:#using else dont make any error
  print("Nothing went wrong")
    
try:
  print(x) # type: ignore
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#Try to open and write to a file that is not writable:
try:
  f = open("Hello there")
  try:
    f.write("Welcome")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
#Raise an exception
#to throw(or raise) an exception, use the raise keyword.
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
#raise keyword is used to raise an exception
x = "Hello"
if not type(x) is int:
    raise TypeError ("Only integers are allowed")