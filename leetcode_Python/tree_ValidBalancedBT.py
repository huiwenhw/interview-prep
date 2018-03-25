'''
https://leetcode.com/problems/balanced-binary-tree/description/
'''

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None: return True

    def findBalanced(node):
        if node is None: return 1

        left = findBalanced(node.left)
        right = findBalanced(node.right)

        if (left == False or right == False):
            return False

        if abs(left - right) > 1:
            return False

        return max(left, right) + 1

    if findBalanced(root) == False:
        return False
    return True

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(isBalanced(root)) # true

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.lright = TreeNode(4)

print(isBalanced(root)) # false
