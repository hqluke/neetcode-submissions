# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # loop through storing node value in a set
        # if we hit the same value again, return true,else false
        values = set()
        while head:
            if head.val not in values or not head.next:
                values.add(head.val)
                if not head.next:
                    return False
                else:
                    head = head.next
            else:
                return True
        return False
