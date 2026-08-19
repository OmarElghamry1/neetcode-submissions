# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root: 
            return []
        from collections import deque

        res = []
        q = deque([root])

        while q: 
            right_side = None
            for i in range(len(q)): 
                cur = q.popleft()
                right_side = cur
                if cur.left: 
                    q.append(cur.left)
                if cur.right: 
                    q.append(cur.right)

            if right_side: 
                res.append(right_side.val)

        return res
                


            

