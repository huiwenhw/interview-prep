'''
https://leetcode.com/problems/pacific-atlantic-water-flow/description/

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# keep two bool matrix for pacific and atlantic
# start from the sides in 
# Check if current index is <= next index. If yes, then dfs 
# loop through both matrix and check if node is True on both matrix
# True, means node is reachable from both sides. add to list
def pacific_atlantic(matrix):
    if not matrix: return []
    rows, cols = len(matrix), len(matrix[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    p_visited = [[False for _ in range(cols)] for _ in range(rows)]
    a_visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = []

    def dfs(i, j, visited):
        visited[i][j] = True
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols and matrix[i][j] <= matrix[next_i][next_j] and not visited[next_i][next_j]:
                dfs(next_i, next_j, visited)

    for i in range(rows):
        dfs(i, 0, p_visited)
        dfs(i, cols-1, a_visited)
    for j in range(cols):
        dfs(0, j, p_visited)
        dfs(rows-1, j, a_visited)
    
    for i in range(rows):
        for j in range(cols):
            if p_visited[i][j] and a_visited[i][j]:
                result.append([i, j])
    return result

def traverse_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    
    # right, up, left, down
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(i, j):
        if (i, j) in visited:
            return 
        visited.add((i, j))
        print('i ', i, ' j ', j, ' matrix[i][j] ', matrix[i][j])
        for direction in directions:
            next_i, next_j = i+direction[0], j+direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                dfs(next_i, next_j)

    for i in range(rows):
        for j in range(cols):
            dfs(i, j)

matrix = [[1,2,2,3,5], [3,2,3,4,4], [2,4,5,3,1], [6,7,1,4,5], [5,1,1,2,4]]
print(pacific_atlantic(matrix))
