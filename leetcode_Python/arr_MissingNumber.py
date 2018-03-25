'''
https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example, 
Given nums = [0, 1, 3] return 2.
n = 3
'''

import sys

def missing_number(nums):
    n = len(nums)
    return n*(n+1)/2 - sum(nums)

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print missing_number(nums)

if __name__ == '__main__':
    main()
