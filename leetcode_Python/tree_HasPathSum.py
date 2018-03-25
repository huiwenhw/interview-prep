'''
https://leetcode.com/problems/path-sum/description/

determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example: given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) time and space 
def haspathsum_short(root, sumn):
    if not root:
        return False

    # only return True if current node is leave 
    if root.left is None and root.right is None and root.val == sumn:
        return True

    sumn -= root.val
    return haspathsum_short(root.left, sumn) or haspathsum_short(root.right, sumn)

def haspathsum(root, sumn):
    if not root: return False
    return findpath(root, 0, sumn)

def findpath(root, curr, sumn):
    print(curr, root.val, sumn)
    if root.left and root.right:
        return findpath(root.left, curr+root.val, sumn) or findpath(root.right, curr+root.val, sumn)
    elif root.left:
        return findpath(root.left, curr+root.val, sumn)
    elif root.right:
        return findpath(root.right, curr+root.val, sumn)
    else:
        if curr + root.val == sumn:
            return True
    return False

root = TreeNode(1)
root.left = TreeNode(2)
print(haspathsum_short(root, 1)) # False
print(haspathsum(root, 1)) # False

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)
print(haspathsum_short(root, 6)) # False 
print(haspathsum(root, 6)) # False 

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.right = TreeNode(2)
root.left.left.left = TreeNode(7)
print(haspathsum_short(root, 22)) # True
print(haspathsum(root, 22)) # True
