# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_order(root):
    if not root: return []
    ans, queue = [], [(root, 0)]
    while queue:
        curr, level = queue.pop(0)
        if len(ans) == level: ans.append([])
        ans[level].append(curr.val)
        if curr.left: queue.append((curr.left, level+1))
        if curr.right: queue.append((curr.right, level+1))
    return ans
