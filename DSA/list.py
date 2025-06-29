#Creating list
x = [] #empty list
y = [1,2,3,4,5]
z = [1,"Ashma", 3.14, True]
print(x)
print(y)
print(z)

#list methods
x = [9, 13,7, 3, 11]
x.append(8)
x.sort()

print(x)

#Create an algorithm
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)

#Stack implementation using python list
stack = [] #push

stack.append('A')
stack.append('B')
stack.append('c')
print("Stack:", stack)

#peek
topElement = stack[-1]
print("Peek:", topElement)
 #pop
poppedElement = stack.pop()
print("pop:", poppedElement)
#stack after pop
print("Stack after pop:", stack)

#isEmpty
isEmpty = not bool(stack)
print("isEmpty:", isEmpty)
 #Size
print("Size:", len(stack))

#creating a stack using class:
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
#create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop:", myStack.pop())
print("Stack after pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())

#creating a stack using a linked list:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    def isEmpty(self):
        return self.size ==0
    def stackSize(self):
        return self.size
    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end="->")
            currentNode = currentNode.next
        print()
        
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("LinkedList:", end="")
myStack.traverseAndPrint()
print("peek:", myStack.peek())
print("pop:", myStack.pop())
print("LinkedList after pop:", end="")
myStack.traverseAndPrint()
print("isEmpty:", myStack.isEmpty())
print("Size:", myStack.stackSize())
    
    
        