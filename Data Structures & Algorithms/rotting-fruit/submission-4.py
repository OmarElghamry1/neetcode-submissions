class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = collections.deque()
        n_fresh = 0
        
        for r in range(m): 
            for c in range(n): 
                if grid[r][c] == 1: 
                    n_fresh += 1
                
                if grid[r][c] == 2: 
                    q.append([r, c])
    
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        time = 0
        while q and n_fresh > 0: 

            for _ in range(len(q)): 
                row, col = q.popleft()

                for dr, dc in directions: 
                    r, c = row + dr, col + dc
                    if (r in range(m) and c in range(n) \
                        and grid[r][c] == 1): 
                            grid[r][c] = 2
                            n_fresh -= 1
                            q.append([r, c])
                
            time += 1


        return time if n_fresh == 0 else -1





        