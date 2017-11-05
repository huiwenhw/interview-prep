# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_valid_bst(root):
    def is_valid(node):
        if node is None:
            return (node, float('inf'), float('-inf'), True)
        lnode, lmin, lmax, lbool = is_valid(node.left)
        if lnode:
            if lnode.val >= node.val or lmax >= node.val:
                return (node, lmin, lmax, False)
            lmin, lmax = min(lmin, lnode.val),  max(lmax, lnode.val)
        rnode, rmin, rmax, rbool = is_valid(node.right)
        if rnode:
            if rnode.val <= node.val or rmin <= node.val:
                return (node, rmin, rmax, False)
            rmin, rmax = min(rmin, rnode.val), max(rmax, rnode.val)
        return (node, min(lmin, rmin), max(lmax, rmax), lbool == rbool)
    return is_valid(root)[3]

def is_valid_short(root):
    def is_valid(node, nmin, nmax):
        if not node:
            return True
        if node.val >= nmin or node.val <= nmax:
            return False
        return is_valid(node.left, min(nmin, node.val), nmax) and is_valid(node.right, nmin, max(nmax, node.val))
    return is_valid(root, float('inf'), float('-inf'))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)

print('is valid bst: ', is_valid_bst(root))
print('is valid bst: ', is_valid_short(root))
