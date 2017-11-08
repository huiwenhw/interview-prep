'''
https://leetcode.com/problems/clone-graph/description/
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# keep a visited dictionary
# traverse through neighbor list
# if neighbor hasnt been visited, add it to visited and queue
# add neighbor to currently clone-ing neighbor list
def clone_bfs(node):
    if not node:
        return node
    q = []
    visited = {node: UndirectedGraphNode(node.label)}
    q.append((node, visited[node]))
    while q:
        curr, clone = q.pop(0)
        for n in curr.neighbors:
            if n not in visited:
                visited[n] = UndirectedGraphNode(n.label)
                q.append((n, visited[n]))
            clone.neighbors.append(visited[n])
    return visited[node]

# keep a visited dictionary
# if node is visited, then return cloned node
# else, create a clone node from current node 
# add it to visited
# for each neighbor, dfs and append returned node/clone to neighbor list
# if no/no more neighbors, return clone
def clone_dfs(node):
    if not node:
        return node
    visited = {}

    def dfs(node, visited):
        if node in visited:
            return visited[node]

        clone = UndirectedGraphNode(node.label)
        visited[node] = clone

        for n in node.neighbors:
            clone.neighbors.append(dfs(n, visited))
        return clone 
    return dfs(node, visited)

def dfs_start(node):
    if not node:
        return node
    visited = {}
    def dfs(node, visited):
        visited[node] = True
        print(node.label)
        for n in node.neighbors:
            if n not in visited:
                dfs(n, visited)
    dfs(node, visited)

# keep a hash to keep track of visited nodes
def bfs(node):
    q = [node]
    visited = {node: True}
    ans = '' 
    while q:
        curr = q.pop(0)
        ans += str(curr.label) + ' '
        neighbors = curr.neighbors
        for n in curr.neighbors:
            if n not in visited:
                visited[n] = True
                q.append(n)
    print(ans)

node = UndirectedGraphNode(1)
a = UndirectedGraphNode(2)
b = UndirectedGraphNode(3)
c = UndirectedGraphNode(4)
node.neighbors = [a, b, c]

d = UndirectedGraphNode(5)
e = UndirectedGraphNode(6)
a.neighbors = [d, e]

first = UndirectedGraphNode(-1)
one = UndirectedGraphNode(1)
first.neighbors = [one]
#bfs(clone_bfs(first))
#dfs_start(clone_bfs(node))
dfs_start(clone_dfs(node))
