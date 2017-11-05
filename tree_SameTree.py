# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('same tree')
print(same_tree(root, root))
print(same_tree_iter(root, root))
print(same_tree_short(root, root))
