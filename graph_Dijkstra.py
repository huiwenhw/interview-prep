'''
https://leetcode.com/problems/network-delay-time/description/

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
'''

from collections import defaultdict 
import heapq

def networkDelayTime(times, N, K):
    """
    :type times: List[List[int]]
    :type N: int
    :type K: int
    :rtype: int
    """
    adj = defaultdict(list)
    for u,v,w in times:
        adj[u].append((v, w))

    pq = []
    heapq.heappush(pq, (0, K))
    dist = {}

    while pq:
        d, curr = heapq.heappop(pq) # find min dist of next node 

        if curr in dist: continue   # means node is visited, no need to visit again 

        dist[curr] = d
        for neighbor,w in adj[curr]:
            if neighbor not in dist:
                heapq.heappush(pq, (dist[curr]+w, neighbor))

    maxn = max(dist.values())
    return maxn if len(dist) == N else -1

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2

# O(E + V^2) time, O(E + V) space. V = N, E = len(times)
# cause we visit every vertex, and finding min dist node is O(V) 
def networkDelayTime(times, N, K):
    """
    :type times: List[List[int]]
    :type N: int
    :type K: int
    :rtype: int
    """
    adj = defaultdict(list)
    for u,v,w in times:
        adj[u].append((v, w))

    curr = K
    unvisited = set(range(1, N+1))
    dist = [float('inf') for _ in range(N+1)]
    dist[curr] = 0

    while unvisited:
        # calc dist for unvisited neighbors 
        for neighbor,weight in adj[curr]:
            if neighbor in unvisited:
                if dist[curr] + weight < dist[neighbor]:
                    dist[neighbor] = dist[curr] + weight
        # remove curr from unvisited set
        unvisited.remove(curr)

        # update curr to next node with min dist 
        minn = float('inf')
        for i in range(len(dist)):
            if dist[i] < minn and i in unvisited:
                curr = i
                minn = dist[i]

        # if curr not updated, means no unvisited neighbors 
        if curr not in unvisited: break

    maxn = max(dist[1:])
    if maxn == float('inf'): return -1
    return maxn

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2
