# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_subtree(s, t):
    def sametree(p, q):
        if p and q:
            return p.val == q.val and sametree(p.left, q.left) and sametree(p.right, q.right)
        return p is q

    if s is None:
        return False
    if sametree(s, t):
        return True
    return is_subtree(s.left, t) or is_subtree(s.right, t)
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
print(is_subtree(root, root2))
