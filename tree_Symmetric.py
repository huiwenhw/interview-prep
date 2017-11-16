'''
https://leetcode.com/problems/symmetric-tree/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    def sym(left, right):
        if not left and not right: 
            return True
        if left and right and left.val == right.val:
            return sym(left.left, right.right) and sym(left.right, right.left)
        return False
    return sym(root, root)

'''
def isTreeSymmetric(t):
    if not t: return True
    if not t.left and not t.right:
        return True
    elif t.left and t.right:
        return symmetric(t.left, t.right)
    else:
        return False

def symmetric(left, right):
    if not left and not right:
        return True
    elif left and right:
        if int(left.value) != int(right.value):
             return False
        return symmetric(left.left, right.right) or symmetric(left.right, right.left)
    else:
        return False
'''

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(isSymmetric(root)) # True 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print(isSymmetric(root)) # False
