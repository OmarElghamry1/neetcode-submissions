# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        res = []
        level = 0

        if root: 
            q.append(root)

        while len(q) > 0: 
            res.append([])
            for _ in range(len(q)): 
                cur = q.popleft()
                res[level].append(cur.val)
                res[level].append
                if cur.left: 
                    q.append(cur.left)
                if cur.right: 
                    q.append(cur.right)
            level +=1

        return res
        