'''
https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1 3 1 1 1 minimizes the sum.
'''

# O(mn) time, O(mn) space
def min_path_sum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for k in range(cols):
            if i == 0 and k == 0:
                dp[i][k] = grid[i][k]
            elif i == 0:
                dp[i][k] = grid[i][k] + dp[i][k-1]
            elif k == 0:
                dp[i][k] = grid[i][k] + dp[i-1][k]
            else:
                dp[i][k] = grid[i][k] + min(dp[i-1][k], dp[i][k-1])
    return dp[rows-1][cols-1]

# O(mn) time, O(2n) space
def min_space(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf') for _ in range(cols)] for _ in range(2)]

    for i in range(rows):
        ir = i%2
        for k in range(cols):
            if i == 0 and k == 0:
                dp[ir][k] = grid[i][k]
            elif i == 0:
                dp[ir][k] = grid[i][k] + dp[ir][k-1]
            elif k == 0:
                dp[ir][k] = grid[i][k] + dp[ir-1][k]
            else:
                dp[ir][k] = grid[i][k] + min(dp[ir-1][k], dp[ir][k-1])
    return dp[ir][cols-1]

# making it look cleaner
def min_clean(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = grid[0][0]
    for i in range(1, cols):
        dp[0][i] = grid[0][i] + dp[0][i-1]
    for i in range(1, rows):
        dp[i][0] = grid[i][0] + dp[i-1][0]
    for i in range(1, rows):
        for k in range(1, cols):
            dp[i][k] = grid[i][k] + min(dp[i-1][k], dp[i][k-1])
    return dp[rows-1][cols-1]

grid = [[1,3,1], [1,5,1], [4,2,1]]
print(min_path_sum(grid))
print(min_space(grid))
print(min_clean(grid))
