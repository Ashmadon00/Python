#file handling in python allows you to read from and write to files
#opening a file
file_object = open('filename', 'mode') #Filename: name of file, mode: mode in which file is opened
# Example: Reading the entire file
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# Example: Reading one line at a time
file = open('example.txt', 'r')
line = file.readline()
print(line)
file.close() #close a file

#write to a file
# Example:Writing to a file(overwrites existing content)
file = open('example.txt', 'w')
file.write("Hello, world!")
file.close()

# Example:Appending to a file (add line to the end)
file = open('example.txt', 'a')
file.write("\nThis is an appended line.")
file.close()

# close a file 
# using with statement 
with open('example2.txt', 'r') as file:
    content = file.readline()
    print(content) 

# exceptional handling when closing a file 
    file = open('example2.txt', 'r')
    content = file.read()
    print(content)
    file.close()

#Working with diff format files
#CSV using csv module
import csv
file = open('file.csv', mode='r')
reader = csv.reader(file)
