'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
You may assume no duplicate exists in the array.

# Use binary search
'''

import sys

def findMin(nums):
    start, end = 0, len(nums)-1
    while start < end:
        mid = (start + end) / 2
        if nums[end] < nums[mid]:
            start = mid+1
        else:
            end = mid
    return nums[start]

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print findMin(nums)

if __name__ == '__main__':
    main()
