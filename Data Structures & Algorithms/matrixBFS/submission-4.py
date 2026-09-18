class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])

        r, c = 0, 0
        if grid[r][c] == 1: 
            return -1

        visit = set()
        q = collections.deque()

        visit.add((r, c))
        q.append([r, c])


        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n_path = 0
        while q: 
            for _ in range(len(q)): 
                row, col = q.popleft()
                if row == n - 1 and col == m - 1: 
                    return n_path
                for dr, dc in directions: 
                    r, c = row + dr, col + dc

                    if (r in range(n) and c in range(m) \
                        and (r, c) not in visit and grid[r][c] == 0): 
                            visit.add((r, c))
                            q.append([r, c])
                        
            n_path += 1
        
        return -1
        

        




        