'''
https://leetcode.com/problems/serialize-and-deserialize-bst/description/
'''

from LevelOrder import level_order
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

# O(n) time and space 
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

# O(n) time and space 
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
            val = vals.popleft() # O(1) 
            node = TreeNode(val)
            node.left = build(vals, minn, val)
            node.right = build(vals, val, maxn)
            return node 
        else: return # not needed actually

    vals = collections.deque(int(val) for val in data.split())
    return build(vals, float('-inf'), float('inf'))

root = TreeNode(10)
root.left = TreeNode(6)
root.right = TreeNode(20)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.right = TreeNode(30)
data = serialize(root)
print('data ', data) # 10 6 5 7 20 30
ans = deserialize(data)
print(level_order(ans)) # [[10], [6, 20], [5, 7, 30]]
