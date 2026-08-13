class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid) # since it is nxn

        # Base cases: start or end is blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1: 
            return -1
            
        # Edge case: 1x1 grid
        if n == 1:
            return 1

        q = deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))

        directions = [ [ 1,  0],  [-1,  0], 
                       [ 0,  1],  [ 0, -1], 
                       [ 1,  1],  [ 1, -1], 
                       [-1,  1],  [-1, -1] ]
        while q: 
            row, col, length = q.popleft()

            if row == n-1 and col == n-1: 
                return length

            for dr, dc in directions: 
                r, c = row + dr, col + dc

                if min(r, c) < 0 or max(r, c) == n : 
                    continue
                 
                if (r, c) not in visited and grid[r][c] == 0: 
                    q.append((r, c, length+1))
                    visited.add((r, c))
                    
        return -1
