'''
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_list_short(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = merge_list_short(l1.next, l2)
    return l1 or l2


def printlist(head):
    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next
    print(ans)

l1 = ListNode(2)
l2 = ListNode(1)

printlist(merge_list_short(l1, l2)) # 1 2
