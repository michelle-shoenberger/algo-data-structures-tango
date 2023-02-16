class Bst:
  def __init__(self):
    self.parent = None

  def insert(self, value):
    #This is where you will insert a value into the Binary Search Tree
    if not self.parent:
      self.parent = Node(value) 
      return
    current = self.parent
    while current.left or current.right:
      if current.data > value:
        if current.left:
          current = current.left
        else:
          break
      else:
        if current.right:
          current = current.right
        else:
          break
    # current is the last node, value is added to one side
    if current.data > value:
      current.left = Node(value)
    else:
      current.right = Node(value)
    return self.parent

  def contains(self, value):
    # this is where you'll search the BST and return TRUE or FALSE if the value exists in the BST
    if self.parent.data == value:
      return True
    current = self.parent
    while current:
      if current.data == value: return True
      if current.data > value:
        current = current.left
      else:
        current = current.right
    return False

  def remove(self, value):
    # this is where you will remove a value from the BST
    # identify node to be removed, then reinsert all child nodes
    current = self.parent
    previous = None
    while current:
      if current.data == value:
        break
      if current.data > value:
        previous = current
        current = current.left
      else:
        previous = current
        current = current.right
    if not current:
      return "Value not found"
    remain_left = current.left
    remain_right = current.right
    if not previous:
      self.parent = None
    else:
      if previous.left == current:
        previous.left = None
      else:
        previous.right = None
    # insert remaining nodes
    remaining = []
    check = [current.left, current.right]
    while len(check)>0:
      if check[0].left is not None:
        check.append(check[0].left)
      if check[0].right is not None:
        check.append(check[0].right)
      remaining.append(check[0].data)
      check.pop(0)
    for data in remaining:
      self.insert(data)
    return self.parent      



  def __str__(self) -> str:
    return f"{self.parent}"



# ----- Node ------
class Node:
  # store your DATA and LEFT and RIGHT values here
  def __init__(self, data, left=None, right=None) -> None:
    self.data = data
    self.left = left
    self.right = right

  def __str__(self) -> str:
    return f"Data: {self.data} Left: ({self.left}) Right: ({self.right})"

tree = Bst()
tree.insert(100)
tree.insert(20)
tree.insert(500)
tree.insert(30)
tree.insert(10)
tree.insert(40)
print(tree.insert(32))
print(tree.contains(40))
print(tree.contains(15))
print(tree.remove(20))
