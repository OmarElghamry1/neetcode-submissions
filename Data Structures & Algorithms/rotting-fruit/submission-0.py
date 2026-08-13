class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid) # rows
        m = len(grid[0]) # columns
        fresh = 0
        q = deque()
        
        for i in range(n): 
            for j in range(m): 
                if grid[i][j] == 1: 
                    fresh +=1
                if grid[i][j] == 2 : 
                    q.append([i, j])

        if fresh == 0: 
            return 0
    
        minutes = 0
        directions = [[1, 0], [-1 ,  0], 
                      [0, 1], [0  , -1]]
        while q and fresh > 0: 
            for _ in range(len(q)): 
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if min(r, c) < 0 or r >= n or c >= m: 
                        continue

                    if grid[r][c] == 1: 
                        q.append([r, c])
                        grid[r][c] = 2
                        fresh -= 1
                                    
            minutes += 1

        
        return minutes if fresh == 0 else -1
                
            
                




        




        