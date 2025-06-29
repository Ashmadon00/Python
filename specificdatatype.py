#If you want to specify the data type, you can use the following constructor functions:

from re import X


x = str("Hello World")
print(type(x))

x = int(20)
print(type(x))

x = float(20.00)
print(type(x))

y = complex(1j)
print(type(y))

x = list(("apple", "banana"))
print(type(x))

y = tuple(("apple", "banana"))
print(type(y))

x=range(8)
print(type(x))

x= dict(name = "Ashma", age = 29)
print(type(x))

x= bool(2)
print(type(x))

y=bytes(3)
print(type(y))

y=bytearray(4)
print(type(y))

z= memoryview(bytes(8))
print(type(z))