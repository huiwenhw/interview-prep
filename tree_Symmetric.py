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

def isSymmetric(root):
    def sym(left, right):
        if not left and not right: 
            return True
        if left and right and left.val == right.val:
            return sym(left.left, right.right) and sym(left.right, right.left)
        return False
    return sym(root, root)

def isSym(left, right):
    if left == None and right == None:
        return True
    elif left == None or right == None:
        return False
    return left.val == right.val and isSym(left.right, right.left) and isSym(left.left, right.right)
    
def isSymmetricShort(root):
    if not root: return True
    return isSym(root.left, root.right)
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(isSymmetric(root)) # True 
print(isSymmetricShort(root)) # True 
print(isSymmetricIter(root)) # True 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print(isSymmetric(root)) # False
print(isSymmetricShort(root)) # False
print(isSymmetricIter(root)) # False
