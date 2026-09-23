class Graph:

    def __init__(self):
        self.edges = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.edges: 
            self.edges[src] = []
        if dst not in self.edges: 
            self.edges[dst] = []
        
        self.edges[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if dst not in self.edges or src not in self.edges: 
            return False

        if dst in self.edges[src]: 
            self.edges[src].remove(dst)
            return True
        
        

    def hasPath(self, src: int, dst: int) -> bool:
        
        return self._dfs(src, dst, set())
    

    def _dfs(self, src, dst, visit):
            if src == dst: 
                return True
            if src in visit: 
                return False

            visit.add(src)
            for s in self.edges[src]: 
                if self._dfs(s, dst, visit): 
                    return True
                    
            return False
        
        

        


    

        


