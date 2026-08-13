"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_copy = {}

        def dfs(node): 
            if node in new_copy: 
                return new_copy[node]
            
            # else copy and run dfs
            new_copy[node] = Node(node.val)
            for n in node.neighbors: 
                new_copy[node].neighbors.append(dfs(n))
            
            return new_copy[node]

        return dfs(node) if node else None


        
        