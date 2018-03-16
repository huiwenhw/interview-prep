'''
https://leetcode.com/problems/move-zeroes/description/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''

def move_short(nums):
    zeroIndex = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[zeroIndex], nums[i] = nums[i], nums[zeroIndex]
            zeroIndex += 1

arr = [0, 0, 1]
move_short(arr)
print(arr) # [1, 0, 0]

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    start, end, count = 0, len(nums), 0
    while start < end:
        if nums[start] == 0:
            nums[:] = nums[:start] + nums[start+1:] + [nums[start]]
            count += 1 
            start -= 1
        if start + count == end: 
            break
        start += 1

arr = [0, 1, 0, 3, 12]
moveZeroes(arr)
print(arr) # [1, 3, 12, 0, 0]
