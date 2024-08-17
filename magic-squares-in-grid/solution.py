"""
Author: Zachary Flohr
Date: 2024-08-17
"""

class Solution:
    """A counter of non-trivial, normal magic squares in a given grid.

    Public Attributes:
        numMagicSquaresInside: Identify and count all 3 x 3 non-trivial,
            normal, contiguous magic square subgrids in a given grid of
            integers.
    """

    def _checkConstraints(self, magic_square: list[list[int]],
                          order: int) -> list[bool]:
        """Determine if magic_square is non-trivial and normal.

        Args:
            magic_square: A subgrid of integers to test against
                magic square criteria.
            order: The order of the magic square.

        Returns:
            The results of the constraint check.
        """
        trivial = False
        normal = True
        normal_range = [1, order ** 2]
        flattened_magic_square = [num for row in magic_square for num in row]
        magic_square_set = set(flattened_magic_square)
        if len(flattened_magic_square) != len(magic_square_set):
            trivial = True
        if (any(num > normal_range[1] or num < normal_range[0]
                for num in flattened_magic_square)):
            normal = False
        return [trivial, normal]

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        """Find and count all non-trivial, normal magic squares in grid.

        Args:
            grid: A grid of integers to examine for magic squares.

        Returns:
            The number of non-trivial, normal magic squares of order 3.
        """
        order = 3 
        magic_squares = 0
        for i in range(len(grid) - order + 1):
            for j in range(len(grid[i]) - order + 1):
                principal_diag_sum, secondary_diag_sum = 0, 0
                magic_sum = None
                trivial = False
                normal = True
                for k in range(order):
                    magic_square = [
                        row[j : j + order] for row in grid[i : i + order]]
                    trivial, normal = (
                        self._checkConstraints(magic_square, order))
                    if trivial or not normal:
                        break
                    row_sum = sum(magic_square[k])
                    col_sum = sum([row[k] for row in magic_square])
                    principal_diag_sum += magic_square[k][k]
                    secondary_diag_sum += magic_square[order - 1 - k][k]
                    if not magic_sum:
                        magic_sum = row_sum
                    if (row_sum != col_sum or magic_sum != row_sum
                            or principal_diag_sum > row_sum
                            or secondary_diag_sum > row_sum):
                        break
                    if k == order - 1:
                        if (principal_diag_sum == secondary_diag_sum 
                                and principal_diag_sum == magic_sum):
                            magic_squares += 1
        return magic_squares
