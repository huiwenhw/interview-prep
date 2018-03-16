'''
https://leetcode.com/problems/maximum-subarray/description/

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

import sys

# O(n) time O(1) space
def max_subarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    currsum, maxn = 0, float('-inf')
    for i in range(len(nums)):
        if currsum + nums[i] > 0:
            currsum += nums[i]
            maxn = max(maxn, currsum)
        else:				# to get max of -ve integers
            currsum = 0
            maxn = max(maxn, nums[i])
    return maxn

def max_subarray_short(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
        print(num, curr_sum, max_sum)
    return max_sum

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print(max_subarray(nums))
    print(max_subarray_short(nums))

if __name__ == '__main__':
    main()
