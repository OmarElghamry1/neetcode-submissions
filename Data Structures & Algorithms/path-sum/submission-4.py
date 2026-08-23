# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def leafsum(root, targetSum):
            if not root:
                return False

            targetSum = targetSum - root.val

            if not root.left and not root.right:
                return targetSum == 0

            if leafsum(root.left, targetSum):
                return True

            if leafsum(root.right, targetSum):
                return True

            return False

        
        # outerfunction return
        return leafsum(root, targetSum)
