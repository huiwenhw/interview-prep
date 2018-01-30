'''
https://leetcode.com/problems/symmetric-tree/description/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# iteration, O(n) time and space
def isSymmetricIter(root):
    if not root: return True
    stack = [root.left, root.right]
    while stack:
        left, right = stack.pop(), stack.pop()
        if left is None and right is None: continue
        elif left == None or right == None: return False
        if left.val != right.val: return False
        stack.extend([left.left, right.right, left.right, right.left])
    return True

# using recursion
def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None: return True
    return sym(root.left, root.right)

def sym(p, q):
    if p and q:
        return p.val == q.val and sym(p.left, q.right) and sym(p.right, q.left)
    return p is q
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(isSymmetric(root)) # True 
print(isSymmetricIter(root)) # True 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print(isSymmetric(root)) # False
print(isSymmetricIter(root)) # False
