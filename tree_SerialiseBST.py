'''
https://leetcode.com/problems/serialize-and-deserialize-bst/description/
'''

import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

# get preorder sequence
def serialize(root):
    """Encodes a tree to a single string.  
    :type root: TreeNode
    :rtype: str
    """
    def preorder(node):
        if node:
            ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        else: return
    ans = []
    preorder(root)
    return ' '.join(ans)

# using preorder sequence, and tracking min/max value
# pop(0) only if min < val < max 
# recurse down the same way to obtain a tree
def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    def build(vals, minn, maxn):
        if len(vals) == 0: return
        val = vals[0]
        if minn < val and val < maxn:
            val = vals.popleft()
            node = TreeNode(val)
            node.left = build(vals, minn, val)
            node.right = build(vals, val, maxn)
            return node 
        else: return

    vals = collections.deque(int(val) for val in data.split())
    return build(vals, float('-inf'), float('inf'))

def level_order(root):
    index = 0
    ans, queue = [], [(root, index)]
    while queue:
        node, level = queue.pop(0)
        if node:
            if len(ans) == level:
                ans.append([])
            ans[level] = ans[level] + [node.val]
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return ans

root = TreeNode(10)
root.left = TreeNode(6)
root.right = TreeNode(20)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.right = TreeNode(30)
data = serialize(root)
print('data ', data)
ans = deserialize(data)
print(level_order(ans))
