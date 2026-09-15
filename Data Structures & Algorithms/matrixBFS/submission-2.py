from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        r, c = 0, 0

        if grid[r][c] == 1: 
            return -1
        
        n, m = len(grid), len(grid[0])
        if n == 1 and m == 1: 
            return 0

        visit = set()
        q = deque()
        q.append([r, c])
        visit.add((r, c))
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        n_path = 0
        while q: 
            for _ in range(len(q)): 
                row, col = q.popleft()
                for dr, dc in directions: 
                    r, c = row + dr, col + dc
                    if (r in range(n) and 
                        c in range(m) and 
                        (r, c) not in visit and 
                        grid[r][c] == 0): 
                            if r == (n - 1) and c == (m - 1): 
                                return n_path+1

                            q.append([r, c])
                            visit.add((r, c))
            n_path+=1
        
        return -1
            




    

        




        