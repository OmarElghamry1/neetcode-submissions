# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self, root): 
        cur = root
        while cur and cur.left: 
            cur = cur.left
        return cur.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: 
            return None

        if key < root.val: 
            root.left = self.deleteNode(root.left, key)

        elif key > root.val: 
            root.right = self.deleteNode(root.right, key)
        

        else: # we found the node
            if not root.left: 
                return root.right
            elif not root.right: 
                return root.left
            else: # we have more than two children
                minNodeVal = self.findMinNode(root.right)
                root.val = minNodeVal
                root.right = self.deleteNode(root.right, minNodeVal)
        return root
        