class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self) -> None:
    self.total = 0
    self.stack = []

  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.stack.append(data)
    self.total +=1
    return self.stack

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.stack.pop()
    self.total -=1
    return self.stack

  def size(self):
    # write your code that returns the size of the Stack
    return self.total

s =Stack()
s.push(5)
print(s.push('a'))
print(s.pop())
print(s.size())
