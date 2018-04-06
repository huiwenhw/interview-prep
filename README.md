# Interview cheatsheet 

Below is a list of topics and their respective useful algorithms and runtimes. All the examples below are specially curated to cover the basics of each topic. Feel free to click on the example links to check out the full version of the algorithm and the respective question.
All code snippets are in Python.  

Check out the leetcode_Python/Javascript folder for answers to leetcode questions in Python and Javascript respectively! 
Note: Javascript questions are still in progress!

Topics covered: [Linkedlist](#linkedlist), [Graph](#graph), [Trees](#trees), [Arrays](#arrays), [Strings](#strings), [DP](#dp), [Math](#math), [Binary](#binary)

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

    if fast is None: return head.next 		# for cases with only 1 node, and n = 1

    while fast.next:
        slow = slow.next
        fast = fast.next 
    slow.next = slow.next.next			# slow is at n-1 node from end of list 
    return head
```

Reverse singly linked list [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/ll_ReverseList.py)
```python
def reverse(head):
  prev = None
  while head:
      curr = head
      head = head.next	# assign head to next node before its reference change
      curr.next = prev
      prev = curr
  return prev
```

### Graph
BFS [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/graph_CloneGraph.py)
```python
# Using the clone graph example
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def clone_bfs(node):
    if not node: return node
    q = []
    visited = {node : UndirectedGraphNode(node.label)}
    q.append((node, visited[node]))
    
    while q:
    	curr, clone = q.pop(0)
	for n in curr.neighbors:
	    if n not in visited:
	        visited[n] = UndirectedGraphNode(n.label)
		q.append((n, visited[n]))
	    clone.neighbors.append(visited[n])
    return visited[node]
```

DFS [Example](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)  
Tip: Use a directions array [[-1,0], [1, 0], [0, 1], [0, -1]] when traversing through matrices  
```python
# Find longest increasing path in a integer matrix 
# nums = [
#  [9,9,4],
#  [6,6,8],
#  [2,1,1]
#  ]
# Given nums above, Return 4. Reason: the longest increasing path is [1, 2, 6, 9]

def longest_path(matrix):
    if matrix == []: return 0
    rows, cols = len(matrix), len(matrix[0])
    memo = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def dfs(i, j, currlen):
    	if memo[i][j] != 0: return memo[i][j]
	
	maxl, returned_len = 0, 0
	directions = ((-1,0), (1, 0), (0, 1), (0, -1))				# for checking all neighbouring cells 
	for direction in directions:
	    next_i, next_j = i + direction[0], j + direction[1]
	    if 0 <= next_i and next_i < rows and 0 <= next_j and next_j < cols:	  # check boundaries
	        if matrix[next_i][next_j] > matrix[i][j]:			  # proceed only if next cell > current cell
		    returned_len = dfs(next_i, next_j, currlen)
	    maxl = max(currlen, returned_len, maxl)
	memo[i][j] = maxl + 1
	return memo[i][j]

    ans = -1
    for p in range(rows):
        for q in range(cols):
	    ans = max(ans, dfs(p, q, 0))
    return ans 
```

Topological Sort: Presents a ordering such that for vertices UV, vertex U always comes before V in the ordering.  
[Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/graph_CourseSchedule.py)  

Topological Sort BFS: Kahn's algorithm, taken from [wiki](https://en.wikipedia.org/wiki/Topological_sorting).  
A topo sort can only occur if and only if graph is a Directed Acyclic Graph. Therefore it must have a start node where it has no incoming edges.
```python
# Given the total number of courses and a list of prerequisite pairs, 
# is it possible for you to finish all courses?
# Given 2, [[1,0],[0,1]] 
# Return False. Reason: To take course 1 you should have finished course 0 and vice versa, impossible.  

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
Topological Sort DFS

Algo: Traverse through each unvisited node.  
If node is visited, return. If node is marked as visiting, cycle is found. Else, mark node as visiting, dfs.  
Done visiting, mark node as visited, add node to ans list.  
```python
# same question as above, this time using dfs to solve

def find_order(numCourses, prerequisites):
    graph = defaultdict(list)
    for u,v in prerequisites:
        graph[u].append(v)
     
    ans = []
    visited = [0 for _ in range(numCourses)]
    
    def dfs(node):
        if visited[node] == 1: 		# node is visited, return True
            return True
        if visited[node] == -1:		# node is still visiting. Cycle detected, return False
            return False
        visited[node] = -1		# mark node as visiting
        
        for nei in graph[node]:
            if dfs(nei) == False:
                return False
        visited[node] = 1		# done visiting, mark node as visited 
        ans.append(node)
        return True

    for i in range(numCourses):		# traverse through each unvisited node 
        if dfs(i) == False:
            return []
    return ans
```

Dijkstra: Finds shortest path between nodes in a weighted graph [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/graph_Dijkstra.py)
```python
# times: list of travel times as directed edges, times[i] = (u, v, w)
# N = num of vertices, K = start node 
# Return min dist to ensure all nodes are traversed 

import heapq
import collections

def networkDelayTime(times, N, K):
    adj = collections.defaultdict(list)		  # convert edge list to adjacency list of u: [(v, w), (v2, w2), ...]
    for u,v,w in times:
        adj[u].append((v, w))

    dist = {}
    pq = []
    heapq.heappush(pq, (0, K))
    
    while pq:
        currdist, currnode = heapq.heappop(pq)    # extract min
        if currnode in dist: continue             # node is visited. since we always extract min, if currnode in dist,
        dist[currnode] = currdist                 # currdist will be more than the min dist of the currnode

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
Tree Traversals - Inorder: Left, Parent, Right [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/tree_TreeTraversals.py)  
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
Runtime for common operators, reference [here](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)  

| Operation | Example | Complexity | Notes |  
|-----------|---------|------------|-------|
| access / Get | li[index] | O(1) | index |
| set | li[index] = val | O(1) | |
| append | li.append(5) | O(1) | Returns nothing |
| pop | li.pop() | O(1) | Pops the last element |
| length | len(li) | O(1) | |
| clear | li.clear() | O(1) | Same as li = [] |
| | | | 
| slice | li[a:b] | O(len(b-a)) | Returns sliced list | 
| extend | li.extend(nlist) | O(len(nlist)) | Returns nothing | 
| construct / convert | list( {1,2,3,4} ) | O(len(set)) | Returns list |
| | | |
| equality check | list1 == list2 | O(N) | | 
| insert | li.insert(0, 10) | O(N) | Insert 10 into 0th position. Returns nothing | 
| copy | a = li.copy() | O(N) | Returns a copy of li | 
| deepcopy | a = copy.deepcopy(li) | O(N) | For compound objects |
| pop(i) | li.pop(0) | O(N) | Pops first element, all other elements have to be shifted up |
| delete | del li[index] | O(N) | Removes element according to index | 
| remove | li.remove(elem) | O(N) | Removes element | 
| min / max | min(li) / max(li) | O(N) | Searches list | 
| reverse | li.reverse() or li[::-1] | O(N) | | 
| contain | x in li / x not in li: | O(N) | | 
| iterate | for x in li: | O(N) | | 
| | | | 
| sort | li.sort() | O(NlogN) | Sorts original list. Returns nothing | 
| sort | sorted(li) | O(NlogN) | Does not sort original list. Returns sorted list | 
  

Binary search [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_FindMin.py)  
```python
# Find minimum of rotated array 
# Given nums = [4 5 6 7 0 1 2], Result = 0

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

Subsets [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/recur_Subsets.py)
```python
# Given [1,2,3], Result = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# start from [[]], loop through nums array

def subsets_iterative(nums):
    ans = [[]]
    for num in nums:
        ans += [item + [num] for item in ans]
    return ans 
```

Permutations [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_Permutations.py)
```python
# Given [1, 2, 3], Result = [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]

def permutation(nums):
    if len(nums) == 0: return [[]]

    perms = [[]]
    for num in nums:
        newperm = []
        for perm in perms:
            for i in range(len(perm)+1):
                newperm.append(perm[:i] + [num] + perm[i:])	# insert num between indexes
        perms = newperm
    return perms 
```

Letter combinations of a phone number [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_LetterCombinations.py)  
```python
# Given: "23", Result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

def letterCombinations(digits):
    if not digits: return []
    mapping = {"2":"abc" , "3":"def" , "4":"ghi" , "5":"jkl" , "6":"mno" , "7":"pqrs" , "8":"tuv" , "9":"wxyz"}

    ans = [""]
    for digit in digits:
        temp = []
        for s in ans:
            temp += [s + ch for ch in mapping[digit]]
        ans = temp
    return ans 
```

Longest consecutive element sequence [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_LongestConsecutive.py)  
```python
# Given [100, 4, 200, 1, 3, 2], Result = 4
# Reason: the longest consecutive elements sequence is [1, 2, 3, 4]
# Algo: convert nums to a set, go through the set
# if curr-1 is not in the set, means its the first element in a sequence 
# keep a count for consecutive elements present in the set 

def longestConsecutive(nums):
    if nums == []: return 0
    d = set(nums)
    maxn = float('-inf')

    for num in d:
        count = 0
        if num-1 not in d:
            temp = num
            while temp in d:
                count += 1
                temp += 1
            maxn = max(maxn, count)

    return maxn
```

Consecutive subarray sum [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_ConsecutiveSum.py)
```python
# Given array and s, find min subarray length where sum of subarray >= s
# Given nums = [2,3,1,2,4,3] s = 7, Result = 2
# the subarray [4,3] has the minimal length

def minSubArrayLen(s, nums):
    start, end = 0, 0
    currsum, length = 0, float('inf')

    while start <= end and end < len(nums):
        if currsum < s:					# add curr elem to currsum and keep going
            currsum += nums[end]
            end += 1
        while currsum >= s:				# shift start pointer right till currsum is < s 
            length = min(length, end - 1 - start + 1)	# keep track of the length
            currsum -= nums[start]
            start += 1

    if length == float('inf'):				# means subarray is not found, length = 0
        return 0
    return length 
```

Maximum sum subarray [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_MaxSumSubarray.py)  
```python
# Find the subarray within an array (containing at least one number) which has the largest sum.
# Given [-2,1,-3,4,-1,2,1,-5,4], Result = 6
# Reason: the subarray [4,-1,2,1] has the largest sum = 6

def max_subarray_short(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

Maximum product subarray [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_MaxProductSubarray.py)  
```python
# Keep big and small product at each element, cause we never know when a negative can become positive 
# Given [-2,3,-4], Result = 24 
# Reason: -2 * 3 * -4 = 24

def max_subarray_short(nums):
    if len(nums) <= 1: return nums[0]
    maxnum = big = small = nums[0]
    for num in nums[1:]:
        big, small = max(num, num*big, num*small), min(num, num*big, num*small)
        maxnum = max(maxnum, big)
    return maxnum
```

Max area between elements a.k.a: Container with most water [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_ContainerWater.py)  
```python
# Given array of heights, each elem represents a point (i, height[i]) 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Given [4, 1, 3, 4], Result = 12 

# Algo: want to find container with max height and max width btwn them 
# start from ends of array, shift shorter side in 
# keep checking the max. stop when we reach the middle 

def maxArea(height):
    start, end = 0, len(height) - 1
    area = float('-inf')

    while start < end:
        h = min(height[start], height[end])
        area = max(area, h * (end-start))
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return area 
```

Largest Rectangle Area [Example](https://github.com/huiwenhw/interview-prep/blob/master/leetcode_Python/arr_LargestRectangleArea.py)  
```python
'''
keep ascending buildings index in a stack
loop: if a descending building is detected, pop out the latest building from the stack
algo checks for every peak in the array and keeps the ascending elements 
once all ascendings buildings are added at index i, check 
use dummy building at the end to calc the 'final' ascending buildings
'''

def area_short(height):
    height.append(0)		# dummy building at the end to calc the 'final' ascending buildings
    stack = [-1]		# dummy first building index
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:	# check curr height against stack of buildings
            h = height[stack.pop()]		# if curr is smaller, pop latest building = h
            w = i - stack[-1] - 1		# get width = curr index - last ascending building index before this - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
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
