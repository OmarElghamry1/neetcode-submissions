class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        prevRow = [0] * (n + 1)
        prevRow[n - 1] = 1

        for r in range(m - 1, -1, -1): 
            curRow = [0] * (n + 1)
            for c in range(n - 1, -1, -1): 
                if obstacleGrid[r][c] == 1: 
                    curRow[c] = 0
                    continue
                
                curRow[c] = prevRow[c] + curRow[c + 1]
            
            prevRow = curRow

        return prevRow[0]







        