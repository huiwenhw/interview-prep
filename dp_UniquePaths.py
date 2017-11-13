'''
https://leetcode.com/problems/unique-paths/description/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

# m = rows, n = cols
# dp[i][k] stores number of unique paths to reach that grid
# and that's a combination of the up and the left grids 
# if its row 0 or col 0, there can only be one way to reach that grid
# initialise row 0 and col 0 to 1 
# O(n^2) time and space 
def paths(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for k in range(n):
            if i == 0:
                dp[i][k] = 1
            elif k == 0:
                dp[i][k] = 1
            else:
                dp[i][k] = dp[i-1][k] + dp[i][k-1]
    return dp[m-1][n-1]

def paths_refactor(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for k in range(1, n):
            dp[i][k] = dp[i-1][k] + dp[i][k-1]
    return dp[m-1][n-1]

# O(mn) time, O(n) space
# init all to 1, start from row 1 col 1
# using just one array, 
def paths_refactor_short(m, n):
    dp = [1] * n
    for i in range(1, m):
        for k in range(1, n):
            dp[k] += dp[k-1]
    return dp[n-1]

print(paths(2,2)) # 2
print(paths(1,2)) # 1 
print(paths_refactor(1,2)) # 1
print(paths_refactor(4,4)) # 20
print(paths_refactor_short(1,2)) # 1
print(paths_refactor_short(2,3)) # 3
