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

        if dst not in self.edges: 
            return False
        
        if src not in self.edges: 
            return False

        
        if dst not in self.edges[src]: 
            return False

        self.edges[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        def dfs(src, target): 

            if src == target: 
                return True

            if src in visit: 
                return False
            

            visit.add(src)

            for nei in self.edges[src]: 
                if dfs(nei, dst): 
                    return True
        
            return False
        
        return dfs(src, dst)


            
        

    