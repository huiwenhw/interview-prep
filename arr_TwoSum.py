'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

import sys 

def two_sum(nums, target):
    i = 0
    length = len(nums)
    while i < length:
        k = i+1
        while k < length:
            if nums[i] + nums[k] == target:
                return [i, k]
            k += 1
        i += 1

def two_sum_dict(nums, target):
    nums_dict = {}
    for i in range(len(nums)):
        if nums[i] in nums_dict:
            return [nums_dict[nums[i]], i]
        nums_dict[target - nums[i]] = i

def main():
    args = sys.argv[1:]
    nums = [int(i) for i in args[0].split(",")]
    # nums = map(int, args[0].split(","))
    target = int(args[1])
    # print two_sum(nums, target)
    print two_sum_dict(nums, target)

if __name__ == '__main__':
    main()
