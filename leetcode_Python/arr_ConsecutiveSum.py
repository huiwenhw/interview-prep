'''
https://leetcode.com/problems/minimum-size-subarray-sum/description/

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''

import sys 

def subarr_sum(s, nums):
    # start from first element, let sum be first elem
    # if sum is smaller than s, continue expanding end 
    # if sum is >= s, keep track of # elem, move start to right
    if len(nums) == 0: return 0
    start = end = 0
    sumn  = nums[0]
    el = float('inf')
    while start <= end and end < len(nums):
        if sumn >= s:
            el = min(el, end-start+1)
            sumn -= nums[start]
            start += 1
        else:
            end += 1
            if end < len(nums):
                sumn += nums[end]
    if el == float('inf'):
        el = 0
    return el

    '''
    tracing:
    start = 0, 1, 2, 3
    end = 0, 1, 2, 3, 4, 5
    sumn = 2, 5, 6, 8, 6, 10, 7, 6, 
    el = inf, 4, 4, 3, 
    '''
def main():
    print(subarr_sum(7, [2,3,1,2,4,3])) # 2

if __name__ == '__main__':
    main()
