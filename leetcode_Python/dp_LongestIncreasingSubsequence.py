'''
https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest increasing subsequence.
For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
'''

# O(n^2) time, O(n) space
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []: return 0
    dp = [0 for _ in range(len(nums))]
    dp[0] = 1

    for i in range(1, len(nums)):
        maxn = 1
        for k in range(i):
            if nums[i] > nums[k]:
                maxn = max(maxn, dp[k] + 1)
        dp[i] = maxn
    return max(dp)

print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])) # 4
print(lengthOfLIS([1,3,6,7,9,4,10,5,6])) # 6

# O(n logn) time, O(n) space
# tails: at i, tails stores the smallest number of each increasing subsequence at length i+1
# if num is larger than all smallest number, append it to the list
# else if num is in btwn a certain tail, tails[i-1] < x <= tails[i], change tails[i]
def lis_short(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = int((i + j) / 2)
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
        print(i, j, tails)
    return size

print(lis_short([10, 9, 2, 5, 3, 7, 101, 18])) # 4
print(lis_short([1, 3, 4, 2, 10])) # 4
