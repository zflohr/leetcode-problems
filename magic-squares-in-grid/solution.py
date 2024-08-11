class Solution:
    """A counter of non-trivial, normal magic squares in a given grid.

    Attributes:
        Public instance methods:
            numMagicSquaresInside: Identify and count all 3 x 3
                non-trivial, normal, contiguous magic square subgrids
                in a given grid of integers.
    """

    def __init__(self) -> None:
        """Initialize the instance."""
        self._magic_order = 3
        self._magic_square_range = [1, self._magic_order ** 2]
        self._grid_col_index, self._grid_row_index = 0, 0
        self._columns_satisfy_magic_square = False
        self._rows_satisfy_magic_square = False
        self._principal_diag_sum, self._secondary_diag_sum = 0, 0
        self._duplicates = False
        self._valid_num_range = True
        self._magic_sum = None
        self._num_magic_squares = 0

    def _checkMagicSquareConstraints(self, magic_square: list[list[int]]):
        """Determine if magic_square is non-trivial and normal.

        Args:
            magic_square: A subgrid of integers to test against
                magic square criteria.
        """
        self._duplicates = False
        self._valid_num_range = True
        flattened_magic_square = [num for row in magic_square for num in row]
        magic_square_set = set(flattened_magic_square)
        if len(flattened_magic_square) != len(magic_square_set):
            self._duplicates = True
        if any(num > self._magic_square_range[1]
                or num < self._magic_square_range[0] for num
                    in flattened_magic_square):
            self._valid_num_range = False

    def _checkMagicSquareColumnSums(self, magic_square: list[list[int]],
                                    magic_index: int):
        """Determine if the column sums in magic_square are equal.

        Args:
            magic_square: A subgrid of integers to test against
                magic square criteria.
            magic_index: The column index of magic_square.
        """
        col_sum = sum([row[magic_index] for row in magic_square])
        if not self._magic_sum:
            self._magic_sum = col_sum
        if self._magic_sum != col_sum:
            self._magic_sum = None
            self._grid_col_index += magic_index
        if magic_index == self._magic_order - 1:
            self._columns_satisfy_magic_square = True

    def _checkMagicSquareRowSums(self, magic_square: list[list[int]],
                                 magic_index: int):
        """Determine if the row sums in magic_square are equal.

        Args:
            magic_square: A subgrid of integers to test against
                magic square criteria.
            magic_index: The row index of magic_square.
        """
        row_sum = sum(magic_square[magic_index])
        if self._magic_sum != row_sum:
            self._magic_sum = None
            self._grid_col_index += 1
            self._columns_satisfy_magic_square = False
        if magic_index == self._magic_order - 1:
            self._rows_satisfy_magic_square = True

    def _checkMagicSquareDiagonalSums(self, magic_square: list[list[int]],
                                      magic_index: int):
        """Determine if the diagonal sums in magic_square are equal.

        Args:
            magic_square: A subgrid of integers to test against
                magic square criteria.
            magic_index: An index used to obtain the diagonals of
                magic_square.
        """
        self._principal_diag_sum += magic_square[magic_index][magic_index]
        self._secondary_diag_sum += magic_square[
                self._magic_order - 1 - magic_index][magic_index]
        if magic_index == self._magic_order - 1:
            self._grid_col_index += 1
            self._columns_satisfy_magic_square = False
            self._rows_satisfy_magic_square = False
            if (self._magic_sum == self._principal_diag_sum
                    and self._magic_sum == self._secondary_diag_sum):
                self._num_magic_squares += 1
            self._principal_diag_sum, self._secondary_diag_sum = 0, 0
            self._magic_sum = None

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        """Find and count all non-trivial, normal magic squares in grid.

        Args:
            grid: A grid of integers to examine for magic squares.

        Returns:
            The number of non-trivial, normal magic squares of order
                self._magic_order in grid.
        """
        self.__init__()
        total_grid_rows = len(grid)
        total_grid_columns = len(grid[0])
        if (total_grid_rows >= self._magic_order
                and total_grid_columns >= self._magic_order):
            while (self._grid_row_index
                    + self._magic_order - 1 < total_grid_rows):
                while (self._grid_col_index
                        + self._magic_order - 1 < total_grid_columns):
                    for magic_index in range(self._magic_order):
                        tested_magic_square = [
                            row[self._grid_col_index : self._grid_col_index
                                    + self._magic_order]
                                for row in grid[
                                    self._grid_row_index : self._grid_row_index
                                        + self._magic_order]]
                        self._checkMagicSquareConstraints(tested_magic_square)
                        if self._duplicates or not self._valid_num_range:
                            self._grid_col_index += 1
                            self._duplicates = False
                            self._valid_num_range = True
                            break
                        if not self._columns_satisfy_magic_square:
                            self._checkMagicSquareColumnSums(
                                tested_magic_square,
                                magic_index)
                            if (not self._magic_sum
                                    or self._columns_satisfy_magic_square):
                                break
                        if (self._columns_satisfy_magic_square
                                and not self._rows_satisfy_magic_square):
                            self._checkMagicSquareRowSums(
                                tested_magic_square,
                                magic_index)
                            if (not self._magic_sum
                                    and not self._columns_satisfy_magic_square
                                    or self._rows_satisfy_magic_square):
                                break
                        if (self._columns_satisfy_magic_square
                                and self._rows_satisfy_magic_square):
                            self._checkMagicSquareDiagonalSums(
                                tested_magic_square,
                                magic_index)
                            if (not self._magic_sum
                                    and not self._columns_satisfy_magic_square
                                    and not self._rows_satisfy_magic_square):
                                break
                self._grid_col_index = 0
                self._grid_row_index += 1
        return self._num_magic_squares
