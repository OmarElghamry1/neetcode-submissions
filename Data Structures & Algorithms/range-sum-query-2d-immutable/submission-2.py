class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m): 
            curRow = 0
            for c in range(n): 
                curRow += matrix[r][c]
                self.prefix[r + 1][c + 1] = curRow + self.prefix[r][c + 1]
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        top_right = self.prefix[r1 - 1][c2]
        bot_left = self.prefix[r2][c1 - 1]
        bot_right = self.prefix[r2][c2]
        top_left = self.prefix[r1 - 1][c1 - 1]

        return bot_right - (top_right + bot_left) + top_left





