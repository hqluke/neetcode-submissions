# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use fast and slow pointers
        # fast pointer will check head.next.next, slow does head.next
        # fast will eventually catch up to slow if it loops

        fast,slow = head,head
        
        # stop loop and return false if no fast.next
        while fast and fast.next:
            # increment pointers
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        