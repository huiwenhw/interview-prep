# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# want to compare right and left, return max 
# keep maxsum check at each node 
# dfs returns both
def max_path_sum(root):
    def dfs(node):
        left = right = 0
        leftsum = rightsum = float('-inf')
        if node.left:
            left, leftsum = dfs(node.left)
            left = max(left, 0)
        if node.right:
            right, rightsum = dfs(node.right)
            right = max(right, 0)
        return node.val + max(left, right), max(node.val + left + right, leftsum, rightsum)
    if root:
        return dfs(root)[1]
    return 0


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('max path sum')
print(max_path_sum(root))
