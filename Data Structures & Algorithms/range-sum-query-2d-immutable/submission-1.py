class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        self.matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m): 
            row_total = 0
            for c in range(n): 
                row_total += matrix[r][c]
                self.matrix[r + 1][c + 1] = row_total + self.matrix[r][c + 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_right = self.matrix[row1][col2 + 1]
        bot_left = self.matrix[row2 + 1][col1]
        top_left = self.matrix[row1][col1]

        return self.matrix[row2 + 1][col2 + 1] - bot_left - top_right + top_left




