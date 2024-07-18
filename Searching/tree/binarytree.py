# A small exercise for us is to add the following functionalities
# find_min()
# find_max()
# calculate_sum()
# pre_order_traversal()
# post_order_traversal()

class BinarySearchTreeNode:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self, data):
    # Since a binary tree can't have duplicate data
    if data == self.data:
      return

    if data < self.data:
      # add data in left subtree
      if self.left: # Checking if any data in self.left
        self.left.add_child(data) # So if data is present we call it recursively until empty node found
      else:
        self.left = BinarySearchTreeNode(data)

    if data > self.data:
      # add data in left subtree
      if self.right: # Checking if any data in self.right
        self.right.add_child(data) # So if data is present we call it recursively until empty node found
      else:
        self.right = BinarySearchTreeNode(data)

  def in_order_traversal(self):
    # Creating an empty list to fill in with elements in correct order
    elements = []

    # Now according to IN ORDER TRAVERSAL: left > base node > right
    # visiting the left tree 
    if self.left: # Going in if any elements in left tree
      elements += self.left.in_order_traversal()

    # visiting base node
    elements.append(self.data)      

    # visiting right tree
    if self.right:
      elements += self.right.in_order_traversal()

    return elements

  def search(self, val):
    if val == self.data:
      return True

    if val < self.data:
      # If val is less than node then it will be present in left node
      if self.left:
        return self.left.search(val)
      else:
        return False

    if val > self.data:
      # If val is more than node then it will be present in right node
      if self.right:
        return self.right.search(val)
      else:
        return False

  def find_min(self):
    min_element = None
    # Checking if self.left is empty or not
    if self.left:
      # If it's not recursively calling find_min() on that node
      # This recursion is basically returning the min_value all the way from the last call of find_min()
      min_element = self.left.find_min()
    else:
      # If there's no further left division add data to min_element
      min_element = self.data

    return min_element
    
  def find_max(self):
    max_element = None
    if self.right:
      max_element = self.right.find_max()
    else:
      max_element = self.data

    return max_element

# A function which takes a list and builds a tree out of it
def build_tree(elements):
  root = BinarySearchTreeNode(elements[0])

  for i in range(1, len(elements)):
    root.add_child(elements[i])

  return root

if __name__=="__main__":
  numbers = [17, 4, 1, 20, 9, 23, 18, 34]
  num_tree = build_tree(numbers)
  # If you notice this in_order_traversal basically gives you a sorted list
  # Also if you pass any duplicates in the list it will only add it once 
  # print("In Order Tranversal: ")
  # print(num_tree.in_order_traversal())

  # search_input = int(input("Enter a number to search: "))
  # print(num_tree.search(search_input))

  # finding minimum
  print(f"Minimum element in num_tree is: {num_tree.find_min()}")
  # finding maximum
  print(f"Maximum element in num_tree is: {num_tree.find_max()}")