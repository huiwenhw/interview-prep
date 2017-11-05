# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
:type root: TreeNode
:rtype: List[int]p
"""
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def inorder_iter(root):
    if root is None: return []
    stack, visited = [root], []
    while stack:
        root = stack[-1]
        if root.left:
            stack.append(root.left)
            root.left = None # so that it will not add back the same node
        else:
            visited.append(stack.pop().val)
            if root.right:
                stack.append(root.right)
                root.right = None 
    return visited

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

def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

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

# add root to ans, then add right and left child 
# always pop left child first
def preorder_iter_short(root):
    ans, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ans

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def postorder_iter(root):
    ans, stack = [], [(root, False)]
    while stack:
        node, visited_twice = stack.pop()
        if node:
            if visited_twice:
                ans.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return ans

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
