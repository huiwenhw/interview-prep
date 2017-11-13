'''
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

# dp[i] contains max amt
# check from dp[0:i-1], what's the max amount
# use that 
# O(n) time and space
def rob(nums):
    if not nums: return 0
    dp = [0] * len(nums)
    for i in range(len(nums)):
        if i-1 > 0:
            dp[i] = nums[i] + max(dp[:i-1])
        else:
            dp[i] = nums[i]
    return max(dp)

# O(n) time, O(1) space
def rob_constant(nums):
    if not nums: return 0
    # dp = [0] * len(nums)
    i = e = 0
    for n in nums:
        i, e = n + e, max(i, e)
    return max(i, e)

print(rob([1,2,1,2,1])) # 4
print(rob([1,2,1,2])) # 4
print(rob([2,1,1,2])) # 4

print(rob_constant([1,2,1,2,1])) # 4
print(rob_constant([1,2,1,2])) # 4
print(rob_constant([2,1,1,2])) # 4
