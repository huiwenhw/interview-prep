'''
https://leetcode.com/problems/course-schedule/description/

There are a total of n courses you have to take, labeled from 0 to n - 1. Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

e.g. 2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
ans: https://discuss.leetcode.com/topic/13412/python-20-lines-dfs-solution-sharing-with-explanation/5
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def can_finish(numCourses, prerequisites):
    adjlist = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

    # build adjlist
    for edge in prerequisites:
        x, y = edge
        adjlist[x].append(y)
    
    def dfs(i, visited, adjlist):
        # if node is being visited, means there's a cycle, ret False
        if visited[i] == -1:
            return False
        # node is visited, don't need to visit again, ret true
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit each neighbor
        neighbors = adjlist[i]
        for n in neighbors:
            if not dfs(n, visited, adjlist):
                return False
        # mark visited when all neighbors are visited
        visited[i] = 1
        return True

    # visit each node
    for i in range(numCourses):
        if not dfs(i, visited, adjlist):
            return False
    return True

"""
# dfs, add v to visited
# go through edgelist, add first v to visited set
# check if second v is in visited
# if second v in visited, then cycled detected
# else, go thru neighbors
def can_finish(numCourses, prerequisites):
    if len(prerequisites) == 0 or numCourses == 0:
        return True

    visited = set()
    reqlist = [[] for i in range(numCourses)]

    for edge in prerequisites:
        reqlist[edge[0]].append(edge[1])

    def dfs(nodeindex, visited, reqlist):
        visited.add(nodeindex)
        neighbors = reqlist[nodeindex]
        print('nodeindex ', nodeindex, ' neighbors ', neighbors, ' visited ', visited)
        for n in neighbors:
            print('neighbour: ' ,n)
            if n not in visited:
                if dfs(n, visited, reqlist) == False:
                    return False
            else:
                return False
        return True

    for num in range(numCourses):
        if num not in visited and reqlist[num]:
            print('dfs index ', num)
            if dfs(num, visited, reqlist) == False:
                return False
        # remove num from reqlist 
        '''
        for i in reqlist:
            if num in i: 
                print('removing ', num)
                i.remove(num)
        '''
    return True
"""

"""
for i in range(len(reqlist)):
     print('i ', i)
     ans = ''
     for el in reqlist[i]:
         ans += str(el) + ' '
     print(ans)
 """

print(can_finish(2, [[1,0]])) # True
print(can_finish(3, [[1,0],[2,0]])) # True
print(can_finish(3, [[0,1],[0,2],[1,2]])) # True
print(can_finish(2, [[1,0],[0,1]])) # False
print(can_finish(4, [[0,1],[1,2],[2,3]])) # True
print(can_finish(4, [[1,0],[2,1],[3,2],[1,3]])) # False
print(can_finish(4, [[0,1],[1,2],[0,3],[3,0]])) # False
