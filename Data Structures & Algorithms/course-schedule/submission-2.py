class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i : [] for i in range(numCourses)}

        for crs, preq in prerequisites: 
            preMap[crs].append(preq)
        

        visit = set()


        def dfs(crs): 
            if crs in visit: 
                return False
            
            # has no preqequsistes
            if len(preMap[crs]) == 0: 
                return True

            visit.add(crs)

            for preq in preMap[crs]: 
                # we can't finish
                if not dfs(preq): 
                    return False
            
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses): 
            # if we can't finish one of them
            if not dfs(crs): 
                return False
        
        return True
                


        

        

        
        

        
        