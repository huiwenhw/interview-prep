'''
https://leetcode.com/problems/number-of-islands/description/
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3
'''

# loop through entire grid, check for 1s 
# dfs through the coords with the 1s and set them to 0s 
# num of times we dfs == num of islands in total
# O(rc)^2?
def islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(i, j):
        # if 0, stop and go back 
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for direction in directions:
            next_i, next_j = i+direction[0], j+direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                dfs(next_i, next_j)

    num = 0
    for i in range(rows):
        for k in range(cols):
            # if 1, search its neighbors, mark neighbors as 0
            if grid[i][k] == 1:
                dfs(i, k)
                num += 1
    return num

grid = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]
print(islands(grid)) # 1
grid = [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]
print(islands(grid)) # 3
grid = [[0,0,0,0,0], [1,1,1,1,1], [0,0,0,0,0], [1,1,1,1,1]]
print(islands(grid)) # 2
