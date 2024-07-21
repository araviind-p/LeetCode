# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            # Compute the depth of each subtree
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            
            # Use the larger one and add 1 for the current node
            return max(lDepth, rDepth) + 1
