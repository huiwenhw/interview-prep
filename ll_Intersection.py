'''
https://leetcode.com/problems/intersection-of-two-linked-lists/description/
Write a program to find the node at which the intersection of two singly linked lists begins.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x 
        self.next = None

# O(n) time, O(1) space 
# check which list has more nodes, traverse for both to reach the same num of nodes
# from there, traverse equally and check when those two nodes are the same
def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    lenA, lenB = 0, 0
    curA, curB = headA, headB
    while curA:
        curA = curA.next
        lenA += 1
    while curB:
        curB = curB.next
        lenB += 1
    curA, curB = headA, headB
    if lenA > lenB:
        for i in range(lenA - lenB):
            curA = curA.next
    elif lenB > lenA:
        for i in range(lenB - lenA):
            curB = curB.next
    while curA != curB:
        curA = curA.next
        curB = curB.next
    return curA

headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(7)
headA.next.next.next.next = ListNode(8)
headA.next.next.next.next.next = ListNode(9)

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = headA.next.next.next
headB.next.next.next = headA.next.next.next.next
headB.next.next.next.next = headA.next.next.next.next.next

curr = getIntersectionNode(headA, headB) # 7 8 9 
while curr:
    print(curr.val)
    curr = curr.next
