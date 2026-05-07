# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the nodes in half
        # reverse the second half
        # merge the two together

        # find middle of nodes
        slow,fast = head, head.next
        # stops when fast reaches end of nodes
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # get the 2nd half (if its odd, 1st half will be longer)
        second = slow.next
        # have the end of the first list point to nothing so we know its the end
        # prev to null because the we're reversing the nodes and the first node on 2nd half should point to nothing
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge lists together
        # prev is now the head of the 2nd half reversed
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        