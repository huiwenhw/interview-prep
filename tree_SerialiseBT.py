'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
'''

from LevelOrder import level_order
import collections 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) time and space 
# 1 2 # # 3 4 # # 5 # # 
def serialise(root):
    def ser(node):
        if node:
            vals.append(str(node.val))
            ser(node.left)
            ser(node.right)
        else:
            vals.append('#')
    vals = []
    ser(root)
    return ' '.join(vals)

# O(n) time and space 
# Changed to not use pop(0) as it is O(n)
# deque makes popleft O(1)
def deserialise(data):
    if not data: return
    def deser(vals):
        if len(vals) == 0: return
        val = vals.popleft() # so that we will go through the array in order
        print(val, vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = deser(vals)
        node.right = deser(vals)
        return node
             
    # vals = data.split()
    vals = collections.deque(data.split())
    return deser(vals)

def deserialise_withiter(data):
    def doit():
        val = next(vals)
        print('val ', val, ' vals ', vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = doit()
        node.right = doit()
        print('node ', node.val)
        return node
    vals = iter(data.split())
    print(data.split())
    return doit()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

data = serialise(root)
print('data ', data) #  1 2 # # 3 4 # # 5 # #
ans = deserialise(data)
print(level_order(ans)) # [[1], [2, 3], [4, 5]]
