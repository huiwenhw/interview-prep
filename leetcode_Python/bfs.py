'''
https://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/
'''

import collections

# using graph as an adjacency list {vertex:[list of edges]}
class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, v):
	# Mark all vertices as not visited 
        visited = [False] * len(self.graph)
        queue = [v]
        visited[v] = True
        
        while queue:
            v = queue.pop(0) # dequeue the first element 
            print(v)
            
            for i in self.graph[v]: # get all neighbors 
                print(i, visited[i], queue)
                if visited[i] == False: # if not visited, mark as visited and append to queue
                    queue.append(i)
                    visited[i] = True

# Driver code
# Create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.bfs(2) #  2 0 3 1 

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def clone_bfs(node):
    if not node:
        return node
    q = []
    visited = {node: UndirectedGraphNode(node.label)} # so that we can do return visited[node]
    q.append((node, visited[node]))
    while q:
        curr, clone = q.pop(0)
        for n in curr.neighbors:
            if n not in visited:
                visited[n] = UndirectedGraphNode(n.label)
                q.append((n, visited[n]))
            clone.neighbors.append(visited[n])
    return visited[node]

one = UndirectedGraphNode(1)
two = UndirectedGraphNode(2)
zero = UndirectedGraphNode(0)
one.neighbors.append(two)
one.neighbors.append(zero)
zero.neighbors.append(one)
zero.neighbors.append(two)
two.neighbors.append(one)
two.neighbors.append(zero)
two.neighbors.append(two)

newnode = clone_bfs(one)
print([x.label for x in newnode.neighbors])


