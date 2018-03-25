'''
https://leetcode.com/problems/product-of-array-except-self/description/

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
'''

import sys

def productExceptSelf(nums):
    arr = []
    curr = 1
    for i in range(len(nums)):
        arr.append(curr)
        curr = curr * nums[i]
        print curr, nums[i]
    print arr
    curr = 1
    for i in range(len(nums)-1, -1, -1):
       arr[i] = arr[i] * curr
       curr = curr * nums[i]
    print arr
    return arr

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print productExceptSelf(nums)

if __name__ == '__main__':
    main()
