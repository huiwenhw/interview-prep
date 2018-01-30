'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 3 cases for max path sum at curr node
# 1: node + left and right children 
# 2: node's left subtree
# 3: node's right subtree

# left, right keeps track of children
# leftsum, rightsum keeps track of left, right subtrees max sum
# leftsum, rightsum used to keep track of max negative num too 
# func returns curr path max, max path sum

# O(n) time and space 
def max_path_sum(root):
    def dfs(node):
        if node is None: return (float('-inf'), float('-inf'))
        left = right = 0
        leftsum = rightsum = float('-inf')
        left, leftsum = dfs(node.left) # leftsum doesn't have max to keep negative numbers 
        left = max(left, 0) # for negative numbers
        right, rightsum = dfs(node.right) # same for rightsum 
        right = max(right, 0) # for negative numbers
        return node.val + max(left, right), max(node.val + left + right, leftsum, rightsum)
    if root:
        return dfs(root)[1]
    return 0


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
print('max path sum ', max_path_sum(root)) # 12

root = TreeNode(-2)
root.left = TreeNode(-1)
print('max path sum ', max_path_sum(root)) # -1
