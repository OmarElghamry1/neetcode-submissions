class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c): 
            if (r in range(m) and c in range(n) \
                and (r, c) not in visit and grid[r][c] == "1"): 
                    visit.add((r, c))
                    return (
                        dfs(r + 1, c),
                        dfs(r - 1, c),
                        dfs(r, c + 1),
                        dfs(r, c - 1)
                        )

        max_area = 0
        for r in range(m): 
            for c in range(n): 
                if grid[r][c] == "1" and (r, c) not in visit: 
                    dfs(r, c)
                    max_area += 1

        return max_area

                    


   
       
            
        

        