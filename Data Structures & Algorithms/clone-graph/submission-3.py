"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # to map old nodes to new nodes, to return same copy 
        node_map = {}

        def dfs(node): 
            if not node: 
                return 
            
            if node in node_map: 
                return node_map[node]
            
            new_node = Node(node.val)
            node_map[node] = new_node

            for nei in node.neighbors: 
                new_node.neighbors.append(dfs(nei))

            return new_node

        
        return dfs(node)

        
   


        


        
        