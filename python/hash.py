class HashTable:
  def __init__(self, number_of_buckets):
    self.number_of_buckets = number_of_buckets
    self.table = [None] * self.number_of_buckets

  def hash(self, value):
    # here is where you'll turn your 'value' into a hash value that will return the index of your table to insert value
    # IMPORTANT: Think about how you'd store values into the same index
    return value % self.number_of_buckets

  def set(self, value):
    # here is where you'll perform your logic to insert the value into your table
    # you'll also call your hash method here to get the index where you'll store the value
    hashidx = self.hash(value)
    self.table[hashidx].append(value)

  def get(self, value):
    # here is where you'll retreive your value from the hash table
    # IMPORTANT: Think about how you'd retreive a value that from an index that has multiple values
    hashidx = self.hash(value)
    if value in self.table[hashidx]:
      return value
    else:
      return "Not found"

  def has_key(self, value):
    # here is where you'll return a True or False value if there is a value stored at a specific index in your HashTable
    hashidx = self.hash(value)
    if value in self.table[hashidx]:
      return True
    else:
      return False
