class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visit = set()

        def dfs(r, c): 

            if not (
                    r in range(rows) \
                    and c in range(cols) \
                    and (r, c) not in visit \
                    and grid[r][c] == 1): 
                    
                    return 0
            
            visit.add((r, c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))
        
        area = 0
        for r in range(rows):
            for c in range(cols): 
                area = max(area, dfs(r, c))
        
        return area
