# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use hashmap to store where the 
        # use two pointers, l at start and r at end
        # store l's next variable in temp and point l to r
        # r points to l's next variable
        if not head:
            return
        l = 0
        mp = {}
        count = 0
        res = node = head
        count = 0
        while head:
            mp[count] = head
            head = head.next
            count += 1
        r = count - 1
        # 2 -> 10 -> 4
        # 4 -> 8 -> 6
        while l < r:
            node = mp[l]
            leftNext = node.next
            rightNode = mp[r]
            node.next = rightNode
            l += 1
            if l >= r:
                break
            rightNode.next = leftNext
            r -= 1
        mp[l].next = None

        