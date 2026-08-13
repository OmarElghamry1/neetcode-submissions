class Graph:
    
    def __init__(self):
        self.edges = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.edges: 
            self.edges[src] = []
        if dst not in self.edges: 
            self.edges[dst] = []
            
        if dst not in self.edges[src]: 
            self.edges[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.edges or dst not in self.edges:
            return False
        try: 
            self.edges[src].remove(dst)
            return True
        except ValueError:
            return False
    
    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        
        def dfs(src, target, visit): 
            if src in visit: 
                return 
            if src == target: 
                return True

            visit.add(src)
            for neighbor in self.edges[src]: 
                if dfs(neighbor, target, visit): 
                    return True
                
            return False
    
        return dfs(src, dst, visit)

        


