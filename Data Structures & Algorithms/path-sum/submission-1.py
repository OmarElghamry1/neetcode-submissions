# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        sum_leaf = []

        def pathsum(root, sum_leaf, targetSum): 
            if root is None: 
                return False
            
            sum_leaf.append(root.val)

            if not root.left and not root.right: 
                if sum(sum_leaf) == targetSum: 
                    return True
                sum_leaf.pop()
                return False

            

            if pathsum(root.left, sum_leaf, targetSum): 
                return True
        

            if pathsum(root.right, sum_leaf, targetSum): 
                return True

            sum_leaf.pop()
            return False

        return pathsum(root, sum_leaf, targetSum)
            

        