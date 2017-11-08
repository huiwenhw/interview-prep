'''
https://leetcode.com/problems/maximum-product-subarray/description/

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
[-2,3,-4] = 24
'''

import sys

# Keep big and small product at each element
# cause we never know when a negative can become positive 
# check maxnum at the end 
def max_subarray_short(nums):
    if len(nums) <= 1: return nums[0]
    maxnum = big = small = nums[0]
    for num in nums[1:]:
        big, small = max(num, num*big, num*small), min(num, num*big, num*small)
        maxnum = max(maxnum, big)
    return maxnum

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print max_subarray_short(nums)

if __name__ == '__main__':
    main()
