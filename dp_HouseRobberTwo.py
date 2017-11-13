'''
https://leetcode.com/problems/house-robber-ii/description/

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

# dp[i] contains max amt
# check from dp[0:i-1], what's the max amount
# O(n) time and space
# take max of nums[1:] and nums[:-1]
def rob(nums):
    def rob_inner(nums):
        print(nums)
        if not nums: return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i-1 > 0:
                dp[i] = nums[i] + max(dp[:i-1])
            else:
                dp[i] = nums[i]
        return max(dp)
    return max(rob_inner(nums[len(nums) != 1:]), rob_inner(nums[:-1]))
    # if my len of nums is 1, take [0:] == nums[0] else, take [1:] == []

def rob_short(nums):
    def rob(nums):
        now = prev = 0
        for n in nums:
            now, prev = max(now, prev+n), now
        return now
    return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))

print(rob([2,1,1,2])) # 3
print(rob([0,0,0])) # 0
print(rob([1,1,1])) # 1
print(rob([1,3,1])) # 3
print(rob([2,7,9,3,1])) # 11
print(rob([1,2,1,1])) # 3

print(rob_short([2,7,9,3,1])) # 11
print(rob_short([1,2,1,1])) # 3
