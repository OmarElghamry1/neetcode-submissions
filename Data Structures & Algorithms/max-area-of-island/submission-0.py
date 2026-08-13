class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c): 
            if (min(r, c) < 0 or r == nrows or c == ncols 
            or grid[r][c] == 0 or (r, c) in visit): 
                return 0

            visit.add((r, c))
            count = 1

            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)

            return count



        area = 0
        for r in range(nrows): 
            for c in range(ncols): 
                if grid[r][c] == 1 and (r, c) not in visit: 
                    area = max(area, dfs(r, c))

        return area
                
        