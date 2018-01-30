'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    index = 0
    ans, queue = [], [root]
    while queue:
        level = []
        num = len(queue)
        for i in range(num):
            curr = queue.pop(0)
            level.append(curr.val)
            if curr.left: queue.append(curr.left) # forgot to check for curr.left/right 
            if curr.right: queue.append(curr.right)
        if index % 2 == 1: level.reverse()
        index += 1
        ans.append(level)
    return ans

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(zigzagLevelOrder(root)) # [[3], [20, 9], [15, 7]]
