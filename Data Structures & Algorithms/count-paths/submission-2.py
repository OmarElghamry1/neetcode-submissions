class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prevRow = [1] * n

        for _ in range(m - 1):
            curRow = [1] * n
            for c in range(n - 2, -1, -1):
                curRow[c] = curRow[c + 1] + prevRow[c]
            prevRow = curRow
        return prevRow[0] 
    

 