class Graph:
    
    def __init__(self):

        self.n = {}

    def addEdge(self, src: int, dst: int) -> None:

        if src not in self.n: 
            self.n[src] = []
        if dst not in self.n: 
            self.n[dst] = []

        self.n[src].append(dst)
        
    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.n or dst not in self.n: 
            return False
        self.n[src].remove(dst)
        return True
 
    def hasPath(self, src: int, dst: int) -> bool:

        visit = set()

        def dfs(src, target): 
            if src in visit: 
                return False

            if src == target: 
                return True
            
            visit.add(src)
            
            for neighbor in self.n[src]: 
                if dfs(neighbor, target): 
                    return True
            
            return False
        
        return dfs(src, dst)

        


