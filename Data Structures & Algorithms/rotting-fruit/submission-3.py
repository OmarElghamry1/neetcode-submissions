class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])

        if n == 0: 
            return -1

        q = collections.deque()
        visit = set()
        
        fresh = 0
        for r in range(n): 
            for c in range(m): 
                if grid[r][c] == 1: 
                    fresh += 1
                if grid[r][c] == 2: 
                    q.append([r, c])

        minutes = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0: 
            for _ in range(len(q)): 
                row, col = q.popleft()
                for dr, dc in directions: 
                    r, c = row + dr, col + dc
                    
                    if (r in range(n) and c in range(m) and 
                        grid[r][c] == 1):
                            grid[r][c] = 2
                            fresh -= 1
                            q.append([r, c])
            minutes += 1
                

        return minutes if fresh == 0 else -1
            








        


                

        
            
                

            
        


       
       


       

       
            
            


            


       