class Graph:

    def __init__(self):
        self.edges = {}
        

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.edges: 
            self.edges[src]= []
        
        if dst not in self.edges: 
            self.edges[dst] = []

        self.edges[src].append(dst)
        
    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.edges or dst not in self.edges: 
            return False

        if dst in self.edges[src]: 
            self.edges[src].remove(dst)
            return True
        
        return False
        

    def hasPath(self, src: int, dst: int) -> bool:
        if self._dfs(src, dst, set()): 
            return True
        
        return False


    def _dfs(self, src, dst, visit): 
        if src in visit: 
            return False
        
        if src == dst: 
            return True

        visit.add(src)

        for nei in self.edges[src]: 
            if self._dfs(nei, dst, visit): 
                return True
            
        return False
        
    

    