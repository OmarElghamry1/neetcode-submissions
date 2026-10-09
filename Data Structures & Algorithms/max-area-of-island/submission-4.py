class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()
        visit = set()

        def _bfs(r, c): 
            q.append([r, c])
            visit.add((r, c))
            area = 1

            while q: 
                for _ in range(len(q)): 
                    row, col = q.popleft()
                    for dr, dc in directions: 
                        r, c = row + dr, col + dc
                        if ( r in range(m) and c in range(n) and \
                            (r, c) not in visit and grid[r][c] == 1):
                                visit.add((r, c))
                                area += 1
                                q.append([r, c])
                                
                                
            return area
        
        max_area = 0
        for r in range(m): 
            for c in range(n): 
                if grid[r][c] == 1 and (r, c) not in visit:  
                    max_area = max(max_area, _bfs(r, c))
        
        return max_area
