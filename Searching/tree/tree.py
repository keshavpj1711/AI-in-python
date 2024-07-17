class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self, child):
    child.parent = self
    self.children.append(child)

  def get_level(self):
    # Now level is simply the number of ancestors a node has
    level = 0 
    
    # What we are doing is if there is parent present we inc level by one 
    # and setting p to the parent itself then for that parent we see if any other parent is present
    p = self.parent
    while p:
      level += 1
      p = p.parent

    return level

  def print_tree(self):
    spaces = " "*self.get_level()*3
    prefix = spaces + "|__" if self.parent else "" # This is basically how we use ternary operator in python
    print(prefix + self.data)
    if self.children:
      for child in self.children:
        child.print_tree()


def build_product_tree():
  root = TreeNode(data="Electronics")
  
  laptop = TreeNode("Laptop")
  laptop.add_child(TreeNode("Macbook"))
  laptop.add_child(TreeNode("Surface Book"))
  laptop.add_child(TreeNode("Thinkpad"))

  mobile = TreeNode("Mobile Phone")
  mobile.add_child(TreeNode("iPhone"))
  mobile.add_child(TreeNode("Pixel"))
  mobile.add_child(TreeNode("Samsung"))

  headphones = TreeNode("Headphones")
  headphones.add_child(TreeNode("Sony"))
  headphones.add_child(TreeNode("Soundcore"))
  headphones.add_child(TreeNode("Boat"))

  root.add_child(laptop)
  root.add_child(mobile)
  root.add_child(headphones)

  return root



if __name__ == "__main__":
  root = build_product_tree()
  root.print_tree()
