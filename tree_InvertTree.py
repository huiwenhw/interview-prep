# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
:type root: TreeNode
:rtype: List[int]p
"""
def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def invert_tree(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left 

    invert_tree(root.left)
    invert_tree(root.right)
    return root

def invert_tree_short(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('invert tree, printed using preorder')
print(preorder(invert_tree(root)))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(preorder(invert_tree_short(root)))
