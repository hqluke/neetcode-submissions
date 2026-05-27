# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative DFS, use a stack
        stack = []
        curr = root
        while curr or stack:
            # go as far left as possible storing each node in the stack
            # curr will eventually get set to None
            while curr:
                stack.append(curr)
                curr = curr.left
            # once we're all the way left, grab most recent node from stack
            # subtract from k to see if we've found the element we need and return it if so
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            # otherwise go to node.right 
            # this will allow us to either find a right node to subtract k from,
            # or move to previous nodes in the stack that we can check.
            curr = curr.right

        