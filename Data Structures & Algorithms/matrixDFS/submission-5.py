class Solution:
    
    def countPaths(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        visit = set()

        def dfs(r, c): 
            if ( r in range(m) and c in range(n) \
                and (r, c) not in visit and grid[r][c] == 0 ): 

                    if r == m - 1 and c == n - 1: 
                        return 1
                    
                    visit.add((r, c))
                    
                    count = 0
                    count += (dfs(r + 1, c) + 
                             dfs(r - 1, c) + 
                             dfs(r, c + 1) + 
                             dfs(r, c - 1) )
                    
                    visit.remove((r, c))
                    return count
                    
            else: 
                return 0
        
        return dfs(0, 0)
        





        
        

        
       