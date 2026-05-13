# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # go through, have a count to know where we're at
        # use L and R pointers
        # dummy points to head so we can return it later
        dummy = ListNode(0,head)
        # left = dummy so we land at the prev node than the one we want to remove
        left = dummy
        right = head
        
        # put the r pointer at the value to remove
        while n > 0:
            right = right.next
            n -= 1
        
        # find the item right before the val to remove
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next

