class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        crsMap = {i: [] for i in range(numCourses)}

        for crs, preq in prerequisites: 
            crsMap[crs].append(preq)
        
        
        visit = set()

        def dfs(crs): 
            if crs in visit: 
                return False
            
            if crsMap[crs] == []: 
                return True
            
            visit.add(crs)

            for preq in crsMap[crs]: 
                if not dfs(preq): 
                    return False
            
            visit.remove(crs)
            crsMap[crs] = []
            return True
        

        for crs in range(numCourses): 
            if not dfs(crs): 
                return False
        
        return True
        





        

        
        

        
        