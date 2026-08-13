# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _inorder(self, root, res): 
        if root is None: 
            return 
        self._inorder(root.left, res)
        res.append(root.val)
        self._inorder(root.right, res)
    

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorder(root, result)
        return result
        

        