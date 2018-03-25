'''
https://leetcode.com/problems/combination-sum-iv/description/

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3], target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.
'''

# dp[i] == how many ways to reach this 
# dp[0] = 0
def combi(nums, target):
    dp = [0] * (target+1)

    for i in range(1, target+1):
        for k in range(len(nums)):
            if i == nums[k]:
                dp[i] += 1
            elif i > nums[k]:
                dp[i] += dp[i-nums[k]]
    return dp[-1]

print(combi([1,2,3], 4))
