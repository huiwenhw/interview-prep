'''
https://leetcode.com/problems/minimum-height-trees/description/
'''

from collections import defaultdict, deque

# there can only be at most two roots in MHT, which are the mid points of the longest path 
# find leaves, remove leaves from neighbours
# keep doing as long as num of nodes is > 2
# ones remaining are the root
def findMinHeightTrees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    adjlist = defaultdict(set)
    for u,v in edges:
        adjlist[u].add(v)
        adjlist[v].add(u)

    nodes = set(range(n)) # {0, 1, 2, 3}
    while len(nodes) > 2:
        leaves = {i for i in nodes if len(adjlist[i]) == 1}
        nodes -= leaves # remove set of leaves from nodes
        for i in leaves:
            for edge in adjlist[i]: # moving up one level 
                adjlist[edge].remove(i)
    return list(nodes)


print(findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])) # [3, 4]

# runs faster due to one lesser for loop, and no set comprehension
def find_min_height_faster(n, edges):
    adjlist = defaultdict(set)
    for u,v in edges:
        adjlist[u].add(v)
        adjlist[v].add(u)
    nodes = set(range(n)) # {0, 1, 2, 3}
    leaves = {i for i in nodes if len(adjlist[i]) == 1}

    while len(nodes) > 2:
        newleaves = set()
        nodes -= leaves
        for i in leaves:
            j = adjlist[i].pop()
            adjlist[j].remove(i)
            print(adjlist)
            if len(adjlist[j]) == 1:
                newleaves.add(j)
        leaves = newleaves
    return list(nodes)


# bfs, O(n^2), TLE
# do bfs on each node to find minheight of each node 
def findMinHeightTrees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    adjlist = defaultdict(list)
    for u,v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)

    levels, ans, minheight = {}, [], float('inf')
    for i in range(n):
        visited, queue = set(), deque([(i, 0)])
        level, height = 0, float('-inf')

        while queue:
            curr, level = queue.popleft()
            visited.add(curr)
            for edge in adjlist[curr]:
                if edge not in visited:
                    queue.append((edge, level+1))
        levels[i] = level
        minheight = min(minheight, level)

    for key, val in levels.items():
        if val == minheight:
            ans.append(key)
    return ans

print(findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])) # [1]
