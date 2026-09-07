from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1
        Q = deque()
        visit = set()
        Q.append((0, 0))
        visit.add((0, 0))
        length = 0

        while Q: 
            for _ in range(len(Q)): 
                r, c = Q.popleft()
                if r == rows - 1 and c == cols - 1: 
                    return length

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions: 
                    nr = r + dr # new row
                    nc = c + dc # new col

                    if not (0 <= nr < rows and 0 <= nc < cols) \
                    or (nr, nc) in visit \
                    or grid[nr][nc] == 1: 
                        continue
                    
                    Q.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        
        return -1
                








        