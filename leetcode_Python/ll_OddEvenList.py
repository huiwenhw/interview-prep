'''
https://leetcode.com/problems/odd-even-linked-list/description/
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(nodes) time and O(1) space
def oddEvenList(head):
    if head is None: return head 

    oddhead = head 
    evenhead = even = head.next 

    while even and even.next:
        head.next = head.next.next # aka even.next
        even.next = even.next.next # will either be a value (odd numbers) or None at the end 
        head, even = head.next, even.next 

    head.next = evenhead
    return oddhead 


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

ans = oddEvenList(head)
while ans is not None:
    print(ans.val)
    ans = ans.next

# O(nodes) time and O(1) space
def oddEvenList(head):
    if head is None or head.next is None: return head 
    oddhead = head 
    evenhead = even = head.next 

    while head.next.next and even.next.next:
        head.next = head.next.next
        even.next = even.next.next
        head, even = head.next, even.next 

    if head.next.next:
        head.next = head.next.next
        head = head.next 
    even.next = None

    head.next = evenhead 
    return oddhead 


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

ans = oddEvenList(head)
while ans is not None:
    print(ans.val)
    ans = ans.next
