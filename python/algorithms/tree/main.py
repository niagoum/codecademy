from tree import *

root1 = TreeNode("A")

root = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
root.children = [three, two]
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
eight = TreeNode("H")
nine = TreeNode("I")
ten = TreeNode("E")

two.children = [five, four]
three.children = [seven, six]
six.children = [eight, nine]
four.children = [ten]

print(root)


res = root.search_return_path("E")

print(res)

