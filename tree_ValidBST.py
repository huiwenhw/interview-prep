'''
https://leetcode.com/problems/validate-binary-search-tree/
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_valid_short(root):
	return isValid(root, float('inf'), float('-inf'))

# O(n)
# not <= cause cant children must be < or > parent
def isValid(root, maxn, minn):
    if not root: return True
    if not (minn < root.val and root.val < maxn):
        return False
    return isValid(root.left, min(maxn, root.val), minn) and isValid(root.right, maxn, max(minn, root.val))

def is_valid_bst(root):
    def is_valid(node):
        if node is None:
            return (node, float('inf'), float('-inf'), True)
        lnode, lmin, lmax, lbool = is_valid(node.left)
        if lnode:
            if lnode.val >= node.val or lmax >= node.val:
                return (node, lmin, lmax, False)
            lmin, lmax = min(lmin, lnode.val),  max(lmax, lnode.val)
        rnode, rmin, rmax, rbool = is_valid(node.right)
        if rnode:
            if rnode.val <= node.val or rmin <= node.val:
                return (node, rmin, rmax, False)
            rmin, rmax = min(rmin, rnode.val), max(rmax, rnode.val)
        return (node, min(lmin, rmin), max(lmax, rmax), lbool == rbool)
    return is_valid(root)[3]

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)

print('is valid bst: ', is_valid_bst(root)) # False
print('is valid bst: ', is_valid_short(root)) # False

root = TreeNode(1)
root.left = TreeNode(1)

print('is valid bst: ', is_valid_bst(root)) # False
print('is valid bst: ', is_valid_short(root)) # False
