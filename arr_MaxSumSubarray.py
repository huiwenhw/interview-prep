'''
https://leetcode.com/problems/maximum-subarray/description/

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

import sys

# maxind is to keep track of negative numbers
def max_subarray(nums):
    curr, maxnum, maxind = 0, 0, float('-inf')
    summed = False
    for num in nums:
        maxind = max(maxind, num)
        if curr + num < 0:
            curr = 0
        else: 
            curr = curr + num
        if curr > maxnum:
            summed = True
            maxnum = curr
    if summed: return maxnum
    return maxind

def max_subarray_short(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
        print num, curr_sum, max_sum
    return max_sum

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print max_subarray(nums)
    print max_subarray_short(nums)

if __name__ == '__main__':
    main()
