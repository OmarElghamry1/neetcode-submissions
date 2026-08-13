class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs_map = {i :[] for i in range(numCourses)} # hashset to store prequisties. 

        for crs, preq in prerequisites: 
            crs_map[crs].append(preq)

        visited = set()
        def dfs(crs):
            if crs in visited: 
                return False
            if crs_map[crs] == []: # doesn't have prequisites
                return True

            visited.add(crs) # now we run dfs
            for preq in crs_map[crs]: 
                if dfs(preq) is False: return False 

            #if we finished all course prequisites
            visited.remove(crs)   
            crs_map[crs] = [] # because if we check again, we don't run dfs 

            return True

        for crs in range(numCourses): 
            if dfs(crs) is False: return False # they could not connected, 
                                               # so we have to check each one
        return True



                

        
                
        



        
        