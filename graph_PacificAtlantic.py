'''
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


"""
# check if curr node is >= all left or top nodes 
# and if curr node is >= all right or bottom nodes 
# if yes, add that to answer 
def pacific_atlantic(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    
    # down, up, right, left
    #directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    pacific_dir = ((0, -1), (-1, 0)) # left, up
    atlantic_dir = ((0, 1), (1, 0)) # right, down

    def dfs(i, j, val, this_dir):
        print('i ', i, ' j ', j, ' matrix[i][j] ', matrix[i][j], ' this_dir ', this_dir)
        if (i, j) in visited:
            return 
        if matrix[i][j] > val:
            return None
        visited.add((i, j))
        if this_dir:
            next_i, next_j = i+this_dir[0], j+this_dir[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                print('this_dir next_i ', next_i, ' next_j ', next_j, ' m[i][j] ', matrix[i][j], ' dir ', this_dir)
                if dfs(next_i, next_j, val, this_dir) is None:
                    return None
        else:
            check, index = [True, True], 0
            for direction in pacific_dir:
                next_i, next_j = i+direction[0], j+direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    print('pacific next_i ', next_i, ' next_j ', next_j, ' m[i][j] ', matrix[i][j], ' dir ', direction)
                    if dfs(next_i, next_j, matrix[i][j], direction) is None:
                        check[index] = False
                        print('pacific none')
                index += 1
            if check[0] == False or check[1] == False: return None
            # if check == [False, False]: return None
            check, index = [True, True], 0
            for direction in atlantic_dir:
                next_i, next_j = i+direction[0], j+direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    print('atlantic next_i ', next_i, ' next_j ', next_j, ' m[i][j] ', matrix[i][j], ' dir ', direction)
                    if dfs(next_i, next_j, matrix[i][j], direction) is None:
                        check[index] = False
                        print('atlantic none')
                index += 1
            if check[0] == False or check[1] == False: return None
            # if check == [False, False]: return None
        return [i, j]

    res, ans = None, []
    for i in range(rows):
        for j in range(cols):
            visited = set()
            print('new')
            res = dfs(i, j, float('inf'), None)
            print('res ' , res)
            if res: ans.append(res)
    return ans
"""

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
