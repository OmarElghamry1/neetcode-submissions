class Solution:
    
    def countPaths(self, grid: List[List[int]]) -> int:
        
        r, c = 0, 0

        if grid[r][c] == 1: 
            return 0
        
        n, m = len(grid), len(grid[0])

        visit = set()

        
        def dfs(r, c): 
            if r in range(n) and c in range(m) \
                and (r, c) not in visit and grid[r][c] == 0: 
                    visit.add((r, c))

                    if r == n - 1 and c == m - 1: 
                        visit.remove((r, c))
                        return 1
                    
                    count = 0
                    count += ( dfs(r + 1, c) + 
                             dfs(r - 1, c) +
                             dfs(r, c + 1) +
                             dfs(r, c - 1) )
                    
                    visit.remove((r, c))

                    return count

            # else not valid path
            return 0

        return dfs(r, c)

        
       