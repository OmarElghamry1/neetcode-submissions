"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: 
            return None
            
        new_to_old = {}

        def dfs(node): 
            if node in new_to_old : 
                return new_to_old[node]
            
            new_node = Node(node.val)

            new_to_old[node] = new_node
            
            for n in node.neighbors: 
                new_node.neighbors.append(dfs(n))
            
            return new_node
        
        return dfs(node)
        

        


        
        