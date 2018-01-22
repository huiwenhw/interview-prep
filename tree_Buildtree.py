# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    return convert(0, len(nums)-1, nums)

def convert(start, end, nums):
    if start > end: return None
    mid = int((start + end) / 2)
    root = TreeNode(nums[mid])
    root.left = convert(start, mid-1, nums)
    root.right = convert(mid+1, end, nums)
    return root

root = sortedArrayToBST([-10,-3,0,5,9])
print(level_order(root))

'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
Given preorder and inorder traversal of a tree, construct the binary tree.
'''

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

preorder = [8,5,9,7,1,12,2,4,11,3]
inorder = [9,5,1,7,2,12,8,4,3,11]
root = build_tree(preorder, inorder)
print(level_order(root))
