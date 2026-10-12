class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])


        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1: 
            return -1 

        q = collections.deque()
        q.append([0, 0])
        visit = set()
        visit.add((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        count = 0
        while q: 
            for _ in range(len(q)): 
                row, col = q.popleft()

                if row == m - 1 and col == n - 1: 
                    return count

                for dr, dc in directions: 
                    r, c = row + dr, col + dc
                    if (r in range(m) and c in range(n) \
                        and (r, c) not in visit and grid[r][c] == 0): 
                           
                            q.append([r, c])
                            visit.add((r, c))
            count += 1

        return -1
                            

        
        




 



        