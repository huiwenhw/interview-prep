'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given a linked list, remove the nth node from the end of list and return its head.
Given linked list: 1->2->3->4->5, and n = 2
After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_nth(head, n):
    prev = dummy = ListNode(float('inf'))
    prev.next = slow = fast = head
    if head.next is None:
        return None
    for i in range(n):
        fast = fast.next
    while fast:
        prev = prev.next
        slow = slow.next
        fast = fast.next
    if prev == dummy:
        head = slow.next
    else:
        prev.next = slow.next
    return head

# without using dummy node 
# if fast is None, just return head.next 
# means we're removing the first element
def remove_nth_short(head, n):
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
    
def printlist(head):
    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next
    print(ans)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next  = ListNode(4)
head.next.next.next.next = ListNode(5)

head1 = ListNode(1)

head2 = ListNode(1)
head2.next = ListNode(2)

printlist(remove_nth(head, 2)) # 1 2 3 5 
printlist(remove_nth(head1, 1)) # None
printlist(remove_nth(head2, 2)) # 2

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next  = ListNode(4)
head.next.next.next.next = ListNode(5)

head1 = ListNode(1)

head2 = ListNode(1)
head2.next = ListNode(2)
printlist(remove_nth_short(head, 2)) # 1 2 3 5 
printlist(remove_nth_short(head1, 1)) # None
printlist(remove_nth_short(head2, 2)) # 2
