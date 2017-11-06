'''
https://leetcode.com/problems/reorder-list/description/
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.
For example, Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# get the middle using slow/fast pointer
# mid, midsec
# reverse the second half using midsec pointer
# 1 2 3 # head: 1, 2. last: 3
# link mid1 - mid while both is not None
# do it in-place, dont return anything
def reorder(head):
    if not head or not head.next:
        return

    # find mid+1 point
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    midsec = slow.next
    slow.next = None
    printlist(head) # 1 2 3 
    printlist(midsec) # 4 5 

    # reverse second half (midsec)
    prev = None
    while midsec:
        curr = midsec
        midsec = midsec.next
        curr.next = prev
        prev = curr
    last = prev
    printlist(last) # 5 4
    
    # link them together
    while head and last:
        curr1, curr2 = head, last
        head, last = head.next, last.next
        curr1.next, curr2.next = curr2, curr1.next
     
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
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
reorder(head)  
printlist(head) # 1 5 2 4 3
reorder(head1) 
printlist(head1) # 1 4 2 3 
