'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# adding by level 
def level_withoutlevel(root):
    if not root: return []
    ans, queue = [], [root]
    while queue:
        level = []
        num = len(queue)
        for i in range(num):
            node = queue.pop(0)
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        ans.append(level)
    return ans
            

# adding per node
def level(root):
    if not root: return []
    ans, queue = [], [(root, 0)]
    while queue:
        curr, level = queue.pop(0)
        if len(ans) == level: ans.append([])
        ans[level].append(curr.val)
        if curr.left: queue.append((curr.left, level+1))
        if curr.right: queue.append((curr.right, level+1))
    return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('level order')
print(level(root))
print(level_withoutlevel(root))
