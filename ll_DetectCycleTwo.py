'''
https://leetcode.com/problems/linked-list-cycle-ii/description/
https://discuss.leetcode.com/topic/17521/share-my-python-solution-with-detailed-explanation

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list. Can you solve it without using extra space?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# dist from head to entry point === dist from where slow meets fast to entry point
# H: dist from head to entry point E
# D: dist from E to X (where slow meets fast)
# slow travelled H+D, fast travelled 2(H+D)
# 2H + 2D = H + D + nLoops -> H = nLoops - D (dist from X to E) 
# so all we gotta do is to find when head meets slow / fast
def detect_short(head):
    loop = None
    slow = fast = head 
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast: 
            loop = slow
            break

    if loop:
        while slow is not head:
            slow = slow.next
            head = head.next
        return slow
    return None

# check if there's loop
# add elements in loop to loopset
# start from head, check if curr in loopset
# first element to be in loopset == entry point
# O(N) time, O(loop) space
def detectCycle(head):
    loop = None
    slow = fast = head 
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast: 
            loop = slow
            break

    if loop:
        curr = loop.next
        loopset = {loop}
        while curr is not loop:
            loopset.add(curr)
            curr = curr.next

        slow = head
        while slow not in loopset:
            slow = slow.next
        return slow
    return None


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next

print(detectCycle(head).val) # 2
print(detect_short(head).val) # 2

head = ListNode(1)
head.next = head

print(detectCycle(head).val) # 1
print(detect_short(head).val) # 1

head = ListNode(1)
head.next = ListNode(2)
head.next.next = head

print(detectCycle(head).val) # 1
print(detect_short(head).val) # 1
