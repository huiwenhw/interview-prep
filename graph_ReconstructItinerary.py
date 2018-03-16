'''
https://leetcode.com/problems/reconstruct-itinerary/description/
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
'''

from collections import defaultdict, deque

# iterative version
def findItinerary(tickets):
    airports = defaultdict(deque)
    tickets.sort()
    for u,v in tickets:
        airports[u].append(v)
    print(airports) #  {'ATL': deque(['JFK', 'SFO']), 'SFO': deque(['ATL']), 'JFK': deque(['ATL', 'SFO'])})

    stack, ans = ["JFK"], []
    while stack:
        while airports[stack[-1]]: # always updates, use the last added to perform dfs
            stack.append(airports[stack[-1]].popleft())
        ans.append(stack.pop()) # no more airports, means we've visited all. add to route
    return ans[::-1] # since we added from the back, reverse list

print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])) # ["JFK","NRT","JFK","KUL"]
print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])) # ["JFK","ATL","JFK","SFO","ATL","SFO"]

# sort tickets according to {airport: lexical order} 
# as we visit a airport, pop it from the dict
# ensures that when we reach that airport again, we know which airport to go next
# we then reverse the visited airports 
def findItinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    airports = defaultdict(deque)
    tickets.sort()
    for u,v in tickets:
        airports[u].append(v)

    ans = []
    def dfs(node):
        while airports[node]: # using while here is impt. ensures tht we cont even if the node we meet is the end airport
            dfs(airports[node].popleft())
        ans.append(node)
    dfs("JFK")
    return ans[::-1]

print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])) # ["JFK","NRT","JFK","KUL"]
print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])) # ["JFK","ATL","JFK","SFO","ATL","SFO"]
