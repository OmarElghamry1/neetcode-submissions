class Solution:
    
    def countPaths(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        
        if grid[0][0] == 1: 
            return 0

        visit = set()
        
        def _dfs(r, c): 
            if ( r in range(n) and c in range(m) 
                and (r, c) not in visit and grid[r][c] == 0 ): 

                if r == n - 1 and c == m - 1: 
                    return 1

                visit.add((r, c))

                count = 0
                count += ( _dfs(r + 1, c) + 
                           _dfs(r - 1, c) + 
                           _dfs(r, c + 1) + 
                           _dfs(r, c - 1) )  
                        

                visit.remove((r, c))

                return count
            # else 
            return 0

        return _dfs(0, 0)

        
        

        
       