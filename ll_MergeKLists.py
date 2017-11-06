'''
https://leetcode.com/problems/merge-k-sorted-lists/description/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# add elements to min-heap
# while heap, pop min, add min to new list
# return list
# complexity: let n be total num of elements.
# O(n log(n)) time complexity O(n) space complexity
def merge(lists):
    minheap = [] 
    dummyhead = dummy = ListNode(float('inf'))
    while True:
        count = 0
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minheap, lists[i].val)
                lists[i] = lists[i].next
                count += 1
        if count == 0:
            break
    while minheap:
        num = heapq.heappop(minheap)
        dummy.next = ListNode(num)
        dummy = dummy.next
    return dummyhead.next

from queue import PriorityQueue

# add first elements of list to priority queue
# while queue is not empty, 
# add next element of smallest element in priority queue to q
# this will ensure we're adding the smaller elements from each list first 
# complexity: let n be total num of elements.
# : O(n log(k)) time and O(k) space complexity
def merge_pqueue(lists):
    dummyhead = dummy = ListNode(float('inf'))
    q = PriorityQueue()
    for node in lists:
        if node:
            q.put((node.val, node))
    while q.qsize() > 0:
        dummy.next = q.get()[1]
        dummy = dummy.next
        if dummy.next: 
            q.put((dummy.next.val, dummy.next))
    return dummyhead.next

def printlist(head): 
    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next
    print(ans)

head = ListNode(-3)
head.next = ListNode(-2)
head.next.next = ListNode(-1)
head.next.next.next  = ListNode(4)
head.next.next.next.next = ListNode(5)

head1 = ListNode(-5)
head1.next = ListNode(1)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(3)

printlist(merge([head, head1]))
printlist(merge_pqueue([head, head1]))
