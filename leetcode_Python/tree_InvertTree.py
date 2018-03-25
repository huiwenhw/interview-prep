'''
https://leetcode.com/problems/invert-binary-tree/description/
'''

from LevelOrder import level_order

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) time 
def invert_tree(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left 

    invert_tree(root.left)
    invert_tree(root.right)
    return root

# has to be on the same line 
def invert_tree_short(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(level_order(invert_tree(root))) # [[1], [3, 2], [5, 4]]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(level_order(invert_tree_short(root))) # [[1], [3, 2], [5, 4]]
