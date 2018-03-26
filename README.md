Below are a list of topics and useful 'must-knows' that I curated specially to check if we've covered the basics we need!  
I'm using Python in all the code snippets below!  
Feel free to click on the example links to check out the actual leetcode question.

Check out the leetcode_Python/Javascript folder for answers to leetcode questions in Python and Javascript respectively! 
Note: Javascript questions are still in progress!

# Topics
### LinkedList
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

Traverse to end of list
```python
while head is not None:
    head = head.next
```

Slow, fast runner to find mid point of linked list
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next 
# slow will be at the mid point of the linked list 
# 1 > 2 > 3 > 4 > 5: slow = 3
# 1 > 2 > 3 > 4: slow = 3
```

Detect cycle [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/ll_DetectCycle.py)
```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 

        if slow is fast:
            return True
    return False
```

Remove nth node from end of list [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/ll_RemoveNthFromList.py)
```python
def remove_nth(head, n):
    slow = fast = head 
    for _ in range(n):
        fast = fast.next

    # for cases with only 1 node, and n = 1
    if fast is None: return head.next 

    while fast.next:
        slow = slow.next
        fast = fast.next 
    # slow is at n-1 node from end of list 
    slow.next = slow.next.next
    return head
```

Reverse singly linked list [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/ll_ReverseList.py)
```python
def reverse(head):
  prev = None
  while head:
      curr = head
      head = head.next
      curr.next = prev
      prev = curr
  return prev
```

### Graph
BFS [Example]()
```python
```

DFS [Example]()  
Tip: Use a directions array [[-1,0], [1, 0], [0, 1], [0, -1]] when traversing through matrices
```python
```

Topological Sort: Presents a ordering such that for vertices UV, vertex U always comes before V in the ordering.  

Topo sort - BFS: Kahn's algorithm, taken from [wiki](https://en.wikipedia.org/wiki/Topological_sorting).  
A topo sort can only occur if and only if graph is a Directed Acyclic Graph. Therefore it must have a start node where it has no incoming edges.
```python
from collections import defaultdict, deque
def find_order(numCourses, prerequisites):
    inedges, outedges = defaultdict(deque), defaultdict(deque)
    
    for u, v in prerequisites:
        inedges[u].append(v)
        outedges[v].append(u)
     
    # finding all nodes with no inedges. start from there 
    queue = deque()
    for num in range(numCourses):
        if num not in inedges:
            queue.append(num)
    
    ans = []
    while queue:
        curr = queue.popleft()
        ans.append(curr)
        
        while outedges[curr]:
            nei = outedges[curr].popleft()    # remove every outgoing edge of curr from the graph
            inedges[nei].remove(curr)         # removing neighbours of curr from inedges list
            if len(inedges[nei]) == 0:        # if curr node has no more inedges, add to queue
                queue.append(nei)
    return ans if len(ans) == numCourses else []
```
Topo sort - DFS

Algo: Traverse through each unvisited node.  
If node is visited, return. If node is marked as visiting, cycle is found. Else, mark node as visiting, dfs.  
Done visiting, mark node as visited, add node to ans list.  
```python
def find_order(numCourses, prerequisites):
    graph = defaultdict(list)
    for u,v in prerequisites:
        graph[u].append(v)
     
    ans = []
    visited = [0 for _ in range(numCourses)]
    
    def dfs(node):
        if visited[node] == 1: 
            return True
        if visited[node] == -1:
            return False
        visited[node] = -1
        
        for nei in graph[node]:
            if dfs(nei) == False:
                return False
        visited[node] = 1
        ans.append(node)
        return True

    for i in range(numCourses):
        if dfs(i) == False:
            return []
    return ans
```

Dijkstra: Finds shortest path between nodes in a weighted graph [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/graph_Dijkstra.py)
```python
import heapq
import collections
# times: List[List[int]], N = num of vertices, K = start node 
# return min dist to ensure all nodes are traversed 
def networkDelayTime(times, N, K):
    # converting edge list to adjacency list of u: [(v, w)]
    adj = collections.defaultdict(list)
    for u,v,w in times:
        adj[u].append((v, w))

    dist = {}
    pq = []
    heapq.heappush(pq, (0, K))
    
    while pq:
        currdist, currnode = heapq.heappop(pq)    # extract min
        if currnode in dist: continue             # node is visited. since we always extract min, this dist will be
        dist[currnode] = currdist                 # more than the one in dist dict 

        for nei,w in adj[currnode]:
            if nei not in dist: 
                heapq.heappush(pq, (currdist + w, nei))   # if node is not visited, add to pq

maxn = max(dist.values())
return maxn if len(dist) == N else -1
```
  
### Trees
```python
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None
```
Tree Traversals - Inorder: Left, Parent, Right  
```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def inorder_iterative(root):
    ans, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            ans.append(temp.val)
            root = temp.right
    return ans 
```
Tree Traversals - Preorder: Parent, Left, Right  
```python
def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def preorder_iterative(root):
    ans, stack = [], [root]
    while stack:
        node = stack.pop()
        if node: 
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ans
```
Tree Traversals - Postorder: Left, Right, Parent  
```python
def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# reverse of (parent, right, left)
def postorder_iterative(root):
    ans, stack = [], [root]
    while stack:
        temp = stack.pop()
        if temp:
            ans.append(temp.val)
            stack.append(temp.left)
            stack.append(temp.right)
    return ans[::-1]

def postorder_iterative(root):
    ans, stack = [], [(root, False)]
    while stack:
        node, visited_twice = stack.pop()
        if node:
            if visited_twice:
                ans.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return ans
```

Definitions of trees 
	- Binary Trees
	- Binary Search Trees
	- Balanced Binary Trees 
	- Balanced Binary Search Trees 
	- Complete Trees
	- Heap 
  BFS 
  DFS 
  
 
### Arrays  
Common operators (insert / delete / append), Reverse / Contain / Iteration  
Runtime for common operators  

Binary search [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_FindMin.py)  
e.g. Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
```python
def find_min(nums):
    start, end = 0, len(nums)-1
    while start < end:
        mid = int((start + end) / 2)
        if nums[end] < nums[mid]:   # rotated, min has to be in btwn mid - end
            start = mid + 1
        else:
            end = mid
    return nums[start]  
```

Subsets
```python
# start from [[]], loop through nums array
def subsets_iterative(nums):
    ans = [[]]
    for num in nums:
        ans += [item + [num] for item in ans]
    return ans 
```

### Strings
Runtime for common string methods  
Permutation [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_Permutations.py)   
```python
def permutations(nums):
    if len(nums) <= 1:
        return [nums]
    
    last = nums[0]
    oldlist = permutations(nums[1:])
    newlist = []
    
    for alist in oldlist:                       # alist is the returned list 
        for index in range(len(alist) + 1):     # for 
            nlist = list(alist)                 # copying alist
            nlist.insert(index, last)           # insert in btwn the curr indexes
            newlist.append(nlist)               # add this list to results
    return newlist

def permutations_iterative(nums):
    if len(nums) == 0: return [[]]
    
    perms = [[]]
    for num in nums:
        newperm = []
        for perm in perms: 
            for i in range(len(perm) + 1):
                newperm.append(perm[:i] + [num] + perm[i:])
        perms = newperm
    return perms
```

### Math
int convert to ascii and vice versa  
```
Convert to ascii: base_ascii = ord(‘a’) # 95
Convert ascii to string: str_ascii = chr(65) # 'A'
```

### Binary 
Convert binary string to int
Convert int to binary 


Operators 
### DP
Memoization 
Top - Down
Bottom - Up 
