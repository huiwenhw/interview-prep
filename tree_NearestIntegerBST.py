'''
Asked in an interview, found the problem set here:
https://practice.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1#ExpectOP
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(logn) time and space, BST 
def search(root, key):
    nearest = bst(root, key, float('inf'), 0)
    return nearest

def bst(root, key, diff, nearestNode):
    if root is None:
        return nearestNode
    if root.val == key:
        return root.val
    
    currdiff = abs(root.val - key)
    print(root.val, key, currdiff, diff)
    if currdiff < diff:
        diff, nearestNode = currdiff, root.val
    
    if root.val < key: 
        return bst(root.right, key, diff, nearestNode)
    return bst(root.left, key, diff, nearestNode)

root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(20)

print(search(root, 4)) # 4 
print(search(root, 15)) # 10
print(search(root, 18)) # 20
print(search(None, 1)) # 0
