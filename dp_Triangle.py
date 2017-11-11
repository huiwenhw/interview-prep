'''
https://leetcode.com/problems/triangle/description/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''

import collections 

# bottom up, O(n^2) space
def minimum_total(triangle):
    if len(triangle) == 1: return triangle[0][0]
    
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    for i in range(len(triangle)-1, -1, -1):
        curr = triangle[i]
        if i == len(triangle)-1:
            dp[i] = list(triangle[i])
            continue
        for k in range(len(curr)):
            dp[i][k] = curr[k] + min(dp[i+1][k], dp[i+1][k+1])
    return dp[0][0]

# bottom up, O(n) space
def minimum_total_short(triangle):
    if not triangle: return
    
    # dont need to check for length, cause this takes in the last array
    # which could also be the first if triangle = [[-10]]
    # and dp[0] will just return -10 cause the loop wont run
    dp = list(triangle[-1]) # list(triangle[-1]) to copy, and not change the original array
    for i in range(len(triangle)-2, -1, -1):
        for k in range(len(triangle[i])):
            dp[k] = triangle[i][k] + min(dp[k], dp[k+1])
    return dp[0]

def min_total_topdown(triangle):
    if not triangle: return 
    dp = [[0 for _ in range(len(row))] for row in triangle]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for k in range(len(triangle[i])):
            if k == 0:
                dp[i][k] = triangle[i][k] + dp[i-1][k]
            elif k == len(triangle[i])-1:
                dp[i][k] = triangle[i][k] + dp[i-1][k-1]
            else:
                dp[i][k] = triangle[i][k] + min(dp[i-1][k-1], dp[i-1][k])
    return min(dp[-1])

triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
print(minimum_total(triangle)) # 11
print(minimum_total_short(triangle)) # 11
print(min_total_topdown(triangle))
