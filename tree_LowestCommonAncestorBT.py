'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) time and space
# if root == None, p or q, 
def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root in [None, p, q]: # same as using == in lists
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left or right

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

p = TreeNode(2)
q = TreeNode(8)

print(lowestCommonAncestor(root, p, q).val)
