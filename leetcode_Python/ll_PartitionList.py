'''
https://leetcode.com/problems/partition-list/description/
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# keep two dummy pointers 
# one for nodes with values < x 
# another for nodes with values >= x 
# stitch left to right, return dummyleft.next
def partition(head, x):
    dummyleft = left = ListNode(float('inf'))
    dummyright = right = ListNode(float('inf'))
    
    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next
        head = head.next
    right.next = None
    left.next = dummyright.next
    return dummyleft.next

def printlist(head): 
    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next
    print(ans)

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next  = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

head1 = ListNode(2)
head1.next = ListNode(1)

printlist(partition(head1, 2))
printlist(partition(head, 3))
