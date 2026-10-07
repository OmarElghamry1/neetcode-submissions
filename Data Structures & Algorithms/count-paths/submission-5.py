class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prevRow = [1] * n
        for r in reversed(range(m - 1)): 
            curRow = [1] * n
            for c in reversed(range(n - 1)): 
                curRow[c] = prevRow[c] + curRow[c+1]

            prevRow = curRow

        return prevRow[0]


        