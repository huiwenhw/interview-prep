'''
https://leetcode.com/problems/rotate-array/description/
'''

# O(n) space, since slicing creates a new copy of the list 
# O(1) time...
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if not nums: return nums
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums) # [5,6,7,1,2,3,4]
