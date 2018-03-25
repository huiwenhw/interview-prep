'''
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# head -> next node | head -> next node 
# want to make the nextnode point to head 
# at every node i'll have head and next 
# want to make next.next = head 
# need to keep pointer of next.next 
# if next node is None, then i stop and return head 
# have the head of the list 
def reverse_list(head):
    prev = None
    nnext = head.next
    while head is not None:
        head.next = prev
        if nnext is not None:
            temp = nnext.next
            nnext.next = head
            #update 
            prev = head
            head = nnext
            nnext = temp
        else:
            break
    return head

# only do it for one node 
def reverse_list_short(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

head = ListNode(1)
head.next = ListNode(2)

print(reverse_list(head).val) # 2
print(reverse_list_short(head).val) # 1 (reversed list)
