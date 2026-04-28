# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # use two pointers, one for each list head
        # compare values, use temp varibles to store next items, point to the lower next value
        # if values are the same just point left to right
        # have node always be the tail
        # dummy points to node
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                # move pointer forward
                list1 = list1.next
            else:
                node.next = list2
                # move pointer forward
                list2=list2.next
            node = node.next
        # if the lists are different values, have either the next node point to the rest of the list
        # or it points to none if they both don't exist
        node.next = list1 or list2

        return dummy.next




        