'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

[1,3], 1 = 0
[3,1], 1 = 1
[4,5,6,7,8,1,2,3], 8 = 4
[1], 0 = -1
'''

import sys

# start <= end so i include the last element for checking
# for [3,1] 1 test case

# nums[start] <= nums[mid] to include  
# for [3,1] 1 test case
# with no = it'll be end=mid-1 but we want start=mid+1
def findRotated(nums, target):
    if len(nums) <= 0: return -1 
    start, end = 0, len(nums)-1
    while start <= end:
        mid = int((start + end) / 2)
        if nums[mid] == target: 
            return mid
        # ascending
        if nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                end = mid-1
            else:
                start = mid+1
        # not ascending
        else:
            if nums[mid] <= target <= nums[end]:
                start = mid+1
            else:
                end = mid-1
    return -1
    
print(findRotated([4,5,6,7,8,1,2,3], 8)) # 4
