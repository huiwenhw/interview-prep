'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
from LevelOrder import level_order

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) time and space
def sorted_short(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums: return None
    mid = int(len(nums) / 2)
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid+1:])
    return node 

# O(n) time and space
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
print(level_order(root)) # [[0], [-10, 5], [-3, 9]]
root2 = sorted_short([-10,-3,0,5,9])
print(level_order(root2)) # [[0], [-10, 5], [-3, 9]]
