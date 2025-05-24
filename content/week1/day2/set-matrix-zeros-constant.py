class Solution:
    def setZeros(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

        # Use first row and first column as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero out cells based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero out first row if needed
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # Zero out first column if needed
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().setZeros(matrix))