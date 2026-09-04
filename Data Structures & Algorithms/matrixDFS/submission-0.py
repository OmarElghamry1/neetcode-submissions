class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(r, c, visit): 
            rows, cols = len(grid), len(grid[0])

            if not (0 <= r < rows and 0 <= c < cols) \
               or grid[r][c] == 1 \
               or (r, c) in visit: 
                return 0

            if r == rows - 1 and c == cols - 1: 
                return 1

            visit.add((r, c))

            count = 0
            count += dfs(r + 1, c, visit)
            count += dfs(r - 1, c, visit)
            count += dfs(r, c + 1, visit)
            count += dfs(r, c - 1, visit)

            visit.remove((r, c))

            return count

        return dfs(0, 0, set())


            
