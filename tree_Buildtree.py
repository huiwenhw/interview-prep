# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if preorder == []:
        return None
    if len(inorder) == 1: 
        return TreeNode(inorder[0])

    root = preorder[0]
    rootindex = inorder.index(root)
    leftinorder = inorder[:rootindex]
    len_left = len(leftinorder)
    rightinorder = inorder[rootindex+1:]
    len_right = len(rightinorder)

    root = TreeNode(root)
    root.left = build_tree(preorder[1:len_left+1], leftinorder)
    root.right = build_tree(preorder[len_left+1:len_left+1+len_right], rightinorder)
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

preorder = [8,5,9,7,1,12,2,4,11,3]
inorder = [9,5,1,7,2,12,8,4,3,11]
root = build_tree(preorder, inorder)
print(level_order(root))
