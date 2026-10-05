class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i: [] for i in range(numCourses)}

        for crs, preq in prerequisites: 
            preMap[crs].append(preq)

        visit = set()

        def _dfs(crs): 
            if crs in visit: 
                return False
            
            if len(preMap[crs]) == []: 
                return True
            
            visit.add(crs)
            
            for preq in preMap[crs]: 
                if not _dfs(preq): 
                    return False
            
            visit.remove(crs)
            preMap[crs] = []

            return True


        for i in range(numCourses): 
            if not _dfs(i): 
                return False
        
        return True
        
        

        
        