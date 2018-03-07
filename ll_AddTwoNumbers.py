'''
https://leetcode.com/problems/add-two-numbers/description/


Given two non-empty linked lists representing two non-negative integers. 
Digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# addends is able to handle multiple linked lists 
# O(n * num of lists), where n is max(l1, l2) 
def addTwoNumbers(l1, l2):
    dummy = curr = ListNode(0)
    carry = 0
    addends = l1, l2 

    while addends or carry:
        carry += sum(a.val for a in addends) # value of linkedlists curr node 
        addends = [a.next for a in addends if a.next] # if linkedlist is empty, won't be inside 
        curr.next = ListNode(carry % 10)
        curr = curr.next
        carry = int(carry / 10)

    return dummy.next

l1 = ListNode(9) 
l1.next = ListNode(9)
l1.next.next = ListNode(9)

l2 = ListNode(1) 
l2.next = ListNode(1)

head = addTwoNumbers(l1, l2) # 0 1 0 1 

while head is not None:
    print(head.val)
    head = head.next
