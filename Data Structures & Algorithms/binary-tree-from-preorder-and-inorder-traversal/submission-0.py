# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # root is first item in preorder
        root = TreeNode(preorder[0])
        # right side of root starts at root
        mid = inorder.index(preorder[0])
        #recursively build left side
        # pre is all left values of root not including root
        # inorder all values to middle
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        # pre is all right values of root
        # post doesn't include middle but all values to the right of it
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
        