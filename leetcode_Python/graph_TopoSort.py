'''
https://leetcode.com/problems/course-schedule-ii/description/
'''

from collections import defaultdict, deque

# O(V + E) time, O(V) space, V = numCourses, E = prereq 
# dfs 
def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    graph = defaultdict(deque)
    for u,v in prerequisites:
        graph[u].append(v)

    ans = []
    visited = [0 for _ in range(numCourses)]

    def dfs(node):
        if visited[node] == -1:     # cycle detected 
            return False 
        if visited[node] == 1:      # node is visited
            return True
        visited[node] = -1          # mark as visiting 
        for neighbor in graph[node]:
            if dfs(neighbor) == False:
                return False

        visited[node] = 1
        ans.append(node)
        return True

    for i in range(numCourses):
        if dfs(i) == False:
            return []

    return ans

print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0, 1, 2, 3]
print(findOrder(3, [[1,0],[1,2],[0,1]])) # []

# O(V + E) time, O(V) space, V = numCourses, E = prereq 
# followed https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    inedges, outedges = defaultdict(deque), defaultdict(deque)

    for u,v in prerequisites:
        inedges[u].append(v)
        outedges[v].append(u)

    queue = deque()
    for num in range(numCourses):
        if num not in inedges:
            queue.append(num)

    ans = []
    while queue:
        curr = queue.popleft()
        ans.append(curr)

        while outedges[curr]:
            a = outedges[curr].popleft()
            inedges[a].remove(curr)
            if len(inedges[a]) == 0:
                queue.append(a)

    return ans if len(ans) == numCourses else []

print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0, 1, 2, 3]
print(findOrder(3, [[1,0],[1,2],[0,1]])) # []
