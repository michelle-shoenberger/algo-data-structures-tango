import copy

class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head=None):
    self.head = head
    self.length = 1 if head else 0

  def append(self, data):
    # write your code to ADD an element to the Linked List - add to end; O(n)
    # data should be a Node
    self.length += 1
    if not self.head:
      self.head = data
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = data
    self.length += 1

  def push(self, data):
    # add to beginning
    # O(1)
    data.next = self.head
    self.head = data
    self.length += 1

  def add(self, data, num):
    # add at Node num, O(n)
    # head is Node 1
    if num > self.length -1: 
      raise IndexError("Out of range")
    if num == 1:
      self.push(data)
      return
    last = self.head
    counter = 2
    while counter < num:
      last = last.next
      counter += 1
    remaining = last.next
    last.next = data
    data.next = remaining
    self.length += 1

  def remove(self, val):
    # remove first Node with val
    # O(n) - traversal to find Node
    current = self.head
    last = None
    while current.next:
      if current.value == val:
        remaining = current.next
        if not last:
          self.head = remaining
          self.length -= 1
          return True
        last.next = remaining
        self.length -= 1
        return True
      last = current
      current = current.next
    return False

  def search(self, val):
    # search for value in nodes
    # O(n) - return boolean
    if not self.head: return False
    current = self.head
    while current.next:
      if current.value == val: return True
      current = current.next
    if current.value == val: return True
    return False

  def get(self, option, num):
    # return either a numbered Node or the Node with the same value
    # option = [index, value]
    if not self.head: return "unable"
    if option == 'index':
      if num > self.length -1: 
        raise IndexError("Out of range")
      current = self.head
      counter = 1
      while counter < num:
        current = current.next
        counter += 1
      return current
    elif option == 'value':
      current = self.head
      while current.next:
        if current.value == num:
          return current
        current = current.next 
      if current.value == num:
        return current
      return "unable to find"
    else:
      return "options are index or value"
        
      


  def __str__(self):
    return f"{self.head}"

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, val, next=None):
    self.value = val
    self.next = next

  def __str__(self):
    return f'Val:{self.value} Next: ({self.next})'



llist = LinkList()
print(llist.search(1))
llist.append(Node(1))
llist.append(Node(2))
llist.append(Node(3))
print(llist)
llist.push(Node(4))
llist.add(Node(5), 2)
print(llist)
llist.remove(5)
print(llist)
print(llist.search(3))
print(llist.get('index', 3))
print(llist.get('value', 1))
