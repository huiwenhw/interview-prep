'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
                   _______6______
                  /              \
               ___2__          ___8__
              /      \        /      \
             0      _4       7       9
                   /  \
                  3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(logn) time 
# if both p and q are smaller than root, go left subtree to check
# if both p and q are larger than root, go right subtree to check
# else, p and q are left children or
# p is root and q is child || q is root and p is child
def lowest_short(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowest_short(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_short(root.right, p, q)
    return root

# if root is p.val or q.val, return p/q
# if both left and right children have value, means p and q is found 
# return current node 
# else, return left or right 
# note: doesnt work if tree is binary tree, cause we're using val here
def lowest(root, p, q):
    if root is None:
        return None

    if root.val == p.val:
        return p
    elif root.val == q.val:
        return q

    left = lowest(root.left, p, q)
    right = lowest(root.right, p, q)

    if left and right:
        return root
    return left or right

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

p = TreeNode(2)
q = TreeNode(8)

print(lowest(root, p, q).val) # 6 
print(lowest_short(root, p, q).val) # 6
