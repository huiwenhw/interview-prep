'''
https://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
'''

import collections 

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list) # dict of lists 

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v):
        # Mark all vertices as not visited 
        visited = [False] * len(self.graph)

        def dfs_recur(v, visited):
            visited[v] = True # Mark current node as visited 
            print(v)
            for i in self.graph[v]:
                if visited[i] == False: # if node is not visited, recur neighbors deep
                    dfs_recur(i, visited) 
        dfs_recur(v, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.dfs(2) # 2 0 1 3 

# also dfs recursive
def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(i, j):
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for direction in directions:
            next_i, next_j = i+direction[0], j+direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                dfs(next_i, next_j)

    num = 0 
    for i in range(rows):
        for k in range(cols):
            if grid[i][k] == "1":
                dfs(i, k) 
                num += 1
    return num 
