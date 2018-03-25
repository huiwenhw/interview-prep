'''
https://leetcode.com/problems/linked-list-cycle/description/

Given a linked list, determine if it has a cycle in it.
Follow up: Can you solve it without using extra space?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# save encountered nodes to a dict and check 
# note: use the ListNode as the key instead of its value
# as there can be duplicate elements
# O(n) time, O(n) space
def detect_cycle(head):
    seen = {}
    index = 0
    while head:
        if head in seen:
            return True
        seen[head] = True
        head = head.next
        index += 1
    return False

# without using extra space:
# changed the value of nodes, which.. probably isn't recommended 
# O(n) time, O(1) space
def detect_cycle_short(head):
    dummy = ListNode(float('inf'))
    while head:
        if head.val == dummy.val:
            return True
        head.val = dummy.val
        head = head.next
    return False

# O(n) time, O(1) space
# will throw exception if fast.next.next is None, 
# and that means we don't have a cycle. so return False
def detect_cycle_s(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

# without using exceptions:
def detect_cycle_ss(head):
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True
    return False


head = ListNode(1)
head.next = head

print(detect_cycle(head))
print(detect_cycle_s(head))
print(detect_cycle_short(head))
