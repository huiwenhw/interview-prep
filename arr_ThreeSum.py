"""
https://leetcode.com/problems/3sum/description/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
    [-1, 0, 1],
    [-1, -1, 2]
]

run: python ThreeSum.py -1,0,1,2,-1,-4

Output:
[-4, -1, -1, 0, 1, 2]
enumerate:  0 -4
x  -1
x  -1
x  0
x  1
x  2
enumerate:  1 -1
x  -1
x  0
x  1
x  2
enumerate:  2 -1
enumerate:  3 0
x  1
x  2
[[-1, -1, 2], [-1, 0, 1]]
"""

import sys 

def three_sum_short(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, num in enumerate(nums[:-2]):
        # skip if previous num is same as the current
        # cause that means we'll be adding the same stuff to set / dict
        if i >= 1 and num == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-num-x] = 1 # need num, x, -num-x = 0
            else:
                res.add((num, -num-x, x))
    return list(res)

def main():
    nums = sys.argv[1].split(",")
    nums = [int(num) for num in nums]
    print(three_sum_short(nums)) # [(-1, -1, 2), (-1, 0, 1)]

if __name__ == '__main__':
    main()
