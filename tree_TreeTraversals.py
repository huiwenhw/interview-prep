'''
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
https://leetcode.com/problems/binary-tree-preorder-traversal/description/
https://leetcode.com/problems/binary-tree-postorder-traversal/description/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
:type root: TreeNode
:rtype: List[int]
"""
# left, root, right
def inorder(root):
    if root is None:
        return [] # forgot the []
    return inorder(root.left) + [root.val] + inorder(root.right)

def inorder_iter_short(root):
    visited, stack = [], [] 
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            visited.append(temp.val)
            root = temp.right
    return visited

# root, left, right
def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# add root to ans, then add right and left child 
# always pop left child first
def preorder_iter_short(root):
    ans, stack = [], [root]
    while root or stack:
        root = stack.pop()
        if root:
            ans.append(root.val)
            stack.append(root.right)
            stack.append(root.left)
    return ans

def preorder_iter(root):
    ans, stack = [], []
    while stack or root:
        if root:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            root = temp.right
    return ans

# left, right, root
def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def postorder_iter(root):
    ans, stack = [], [(root, False)]
    while stack:
        node, visited_twice = stack.pop()
        if node: # left this out
            if visited_twice:
                ans.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return ans

# reverse of root, right, left 
def postorder_iter_short(root):
    ans, stack = [], []
    while root or stack:
        if root:
            ans.append(root.val)
            stack.append(root.left)
            stack.append(root.right)
        root = stack.pop()
    return ans[::-1]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('inorder')
print(inorder(root))
print(inorder_iter(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorder_iter_short(root))

print('preorder')
print(preorder(root))
print(preorder_iter(root))
print(preorder_iter_short(root))

print('postorder')
print(postorder(root))
print(postorder_iter(root))
print(postorder_iter_short(root))
