# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # have variables to know where you are
        # prev = None, curr = head
        # loop through the list
        # while curr:
        # have a temp variable to store the current node
        # temp = curr.next
        # move to head->next (i know thats the cpp syntax for it)
        # next = curr.next
        # swap values
        # prev = curr
        # curr = temp
        
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            
            
