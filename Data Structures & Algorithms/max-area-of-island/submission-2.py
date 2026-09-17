class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        visit = set()

        def dfs(r, c): 
            if r in range(n) and c in range(m) and \
               grid[r][c] == 1 and (r, c) not in visit: 
                    visit.add((r, c))
        
                    return (1 + dfs(r + 1, c) + 
                                dfs(r - 1, c) + 
                                dfs(r, c + 1) + 
                                dfs(r, c - 1)
                            )
            return 0

        max_area = 0
        for r in range(n): 
            for c in range(m): 
                if grid[r][c] == 1: 
                    max_area = max(max_area, dfs(r, c))

        return max_area