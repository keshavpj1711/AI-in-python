class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self, child):
    child.parent = self
    self.children.append(child)


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
  pass