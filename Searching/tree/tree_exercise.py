# To achieve: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self, child):
    child.parent = self
    self.children.append(child)

  def get_level(self):
    level = 0

    p = self.parent
    while p:
      level += 1 
      p = p.parent

    return level

  def print_tree(self, type):
    if type == "name":
      data = self.data[0]
    elif type == "designation":
      data = self.data[1]
    elif type == "both":
      data = self.data[0] + f"({self.data[1]})"
    else:
      print("Please provide a valid arguement in print_tree()")
      data = self.data[0] + f"({self.data[1]})"

    spaces = " "*self.get_level()*3
    prefix = spaces + "|__" if self.parent else ""
    print(prefix + data)
    for child in self.children:
      child.print_tree(type)


def build_management_tree():
  # Root node
  ceo = ["Keshav", "CEO"]
  root = TreeNode(ceo)

  # Cto Node
  cto_node = TreeNode(["Sparsh", "CTO"])
  
  # Child for CTO Node
  infra_head = TreeNode(["Anu", "Infrastructure Head"])
  # Child for infrahead Node
  infra_head.add_child(TreeNode(["Priyansh", "Cloud Manager"]))
  infra_head.add_child(TreeNode(["Madhav", "App Manager"]))

  application_head = TreeNode(["Uttkarsh", "Application Head"])

  # Adding child to CTO Node
  cto_node.add_child(infra_head)
  cto_node.add_child(application_head)

  # HR Head
  hr_node = TreeNode(["Uday", "HR Head"])

  # Adding child for HR head
  hr_node.add_child(TreeNode(["Khusi", "Recruitement Manager"]))
  hr_node.add_child(TreeNode(["Manan", "Policy Manager"]))

  # Adding child to root node 
  root.add_child(cto_node)
  root.add_child(hr_node)

  return root


if __name__ == "__main__":
  root_node = build_management_tree()
  type_input = input("Enter the form of output you want(name/designation/both): ")
  root_node.print_tree(type_input)