'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
Given preorder and inorder traversal of a tree, construct the binary tree.
'''
from LevelOrder import level_order

class TreeNode(object):
    def __init__(self, x): 
        self.val = x 
        self.left = None
        self.right = None

# O(n) time and space
# everytime we pop from preorder, the next one will be the root again
def build_short(preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0)) # find root 
        root = TreeNode(inorder[ind])
        root.left = build_short(preorder, inorder[:ind]) 
        root.right = build_short(preorder, inorder[ind+1:])
        return root

preorder = [8,5,9,7,1,12,2,4,11,3]
inorder = [9,5,1,7,2,12,8,4,3,11]
root = build_short(preorder, inorder)
print(level_order(root)) # [[8], [5, 4], [9, 7, 11], [1, 12, 3], [2]]

# O(n) time and space
def build_tree(preorder, inorder):
    if preorder == []:
        return None
    if len(inorder) == 1: 
        return TreeNode(inorder[0])

    root = preorder[0]
    rootindex = inorder.index(root)
    leftinorder = inorder[:rootindex]
    len_left = len(leftinorder)
    rightinorder = inorder[rootindex+1:]
    len_right = len(rightinorder)

    root = TreeNode(root)
    root.left = build_tree(preorder[1:len_left+1], leftinorder)
    root.right = build_tree(preorder[len_left+1:len_left+1+len_right], rightinorder)
    return root

preorder = [8,5,9,7,1,12,2,4,11,3]
inorder = [9,5,1,7,2,12,8,4,3,11]
root = build_tree(preorder, inorder)
print(level_order(root)) # [[8], [5, 4], [9, 7, 11], [1, 12, 3], [2]]
