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
                
def max_depth(root):
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

def same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)

def same_tree_iter(p, q):
    stack = [(p, q)]
    while stack:
        n, m = stack.pop()
        if n and m:
            if n.val != m.val:
                return False
            stack.append((n.right, m.right))
            stack.append((n.left, m.left))
        elif n is not m:
            return False
    return True

def same_tree_short(p, q):
    # checking if both nodes are None
    if p and q:
        return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)
    # checking p == q, but using reference 
    return p is q

def invert_tree(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left 

    invert_tree(root.left)
    invert_tree(root.right)
    return root

def invert_tree_short(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root

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

'''
def max_path_sum(root):
    ans, stack = [], [(root, None, False)]
    c1, c2, curr, maxsum, curr_parent = 0, 0, 0, 0, None
    while stack:
        node, parent, visited_twice = stack.pop()
        if node: 
            print('node ', node.val, ' visited_twice ', visited_twice)
            print('c1 ', c1, ' c2 ', c2, ' maxsum ', maxsum)
            if parent is None and visited_twice:
                maxsum = max(maxsum, node.val + c1 + c2)
            elif visited_twice:
                if c1 is None and c2 is None:
                    curr_parent = parent
                elif parent == curr_parent:
                    if c1 is None:
                        c1 = node.val
                    elif c2 is None:
                        c2 = node.val
                else:
                    curr_parent = parent
                    maxsum = max(node.val + c1 + c2, maxsum)
                    c1 = max(node.val + c1, node.val + c2)
                    c2 = 0
                print('in visited node ', node.val, ' parent ', parent.val , ' visited_twice ', visited_twice)
                print('in visited c1 ', c1, ' c2 ', c2, ' maxsum ', maxsum, ' currparent ', curr_parent.val)
            else:
                stack.append((node, parent, True))
                stack.append((node.right, node, False))
                stack.append((node.left, node, False))
    return maxsum
'''

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

print('max depth of tree: ', max_depth(root))

print('same tree')
print(same_tree(root, root))
print(same_tree_iter(root, root))
print(same_tree_short(root, root))

print('invert tree, preorder')
print(preorder(invert_tree(root)))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(preorder(invert_tree_short(root)))

print('level order')
print(level_order(root))

print('max path sum')
print(max_path_sum(root))
