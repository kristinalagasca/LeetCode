"""
Given a two-dimensional integer matrix, sort each of the columns in ascending order.

Constraints:
n, m ≤ 250 where n and m are the number of rows and columns in matrix
"""

class Solution:
    def solve(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        res = [[0] * C for _ in range(R)]
        for col in range(C):
            values = [r[col] for r in matrix]
            values.sort(reverse=True)
            for row in range(R):
                res[row][col] = values.pop()
        return res
