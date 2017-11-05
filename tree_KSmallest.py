'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# check left children. if found, return left immediately 
# else, left child returned, add 1 to count and check == k
# check right children. if found, return immediately
# return (node, count, true), keep a boolean to check if element has been found 
# check if boolean is true first
# check if node is none, return count 
def kth_smallest(root, k):
    def kth(node, k, count, found):
        if found or node is None:
            return (node, count, found)
        lnode, count, found = kth(node.left, k, count, found)
        if found:
            return (lnode, count, found)
        else: 
            count += 1
            if count == k:
                return (node, count, True)
        rnode, count, found = kth(node.right, k, count, found)
        if rnode and found:
            return (rnode, count, True)
        return (node, count, found)
    return kth(root, k, 0, False)[0].val

# or just use inorder and check! 
def kth_smallest_short(root, k):
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            if k == 1:
                return root.val
            k -= 1
            root = root.right


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

root1 = TreeNode(1)
root1.right = TreeNode(2)

root2 = TreeNode(2)
root2.left = TreeNode(1)

print('kth smallest: ', kth_smallest(root, 4)) # 4?
print('kth smallest: ', kth_smallest(root1, 2)) # 2
print('kth smallest: ', kth_smallest(root2, 1)) # 1 
print('kth smallest: ', kth_smallest_short(root, 4)) # 4?
print('kth smallest: ', kth_smallest_short(root1, 2)) # 2
print('kth smallest: ', kth_smallest_short(root2, 1)) # 1 
