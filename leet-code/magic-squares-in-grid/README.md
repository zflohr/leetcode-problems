# Magic Squares in Grid

A `3 x 3` **magic square** is a `3 x 3` grid filled with distinct numbers
**from** 1 **to** 9 such that each row, column, and both diagonals all have the
same sum.

Given a `row x col` `grid` of integers, how many `3 x 3` contiguous magic square
subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, `grid` may
contain numbers up to 15.

## Example 1:
<table>
    <tr>
        <td>
            4
        </td>
        <td>
            3
        </td>
        <td>
            8
        </td>
        <td>
            4
        </td>
    </tr>
    <tr>
        <td>
            9
        </td>
        <td>
            5
        </td>
        <td>
            1
        </td>
        <td>
            9
        </td>
    </tr>
    <tr>
        <td>
            2
        </td>
        <td>
            7
        </td>
        <td>
            6
        </td>
        <td>
            2
        </td>
    </tr>
</table>

**Input:** grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]

**Output:** 1

**Explanation:**

The following subgrid is a 3 x 3 magic square:

<table>
    <tr>
        <td>
            4
        </td>
        <td>
            3
        </td>
        <td>
            8
        </td>
    </tr>
    <tr>
        <td>
            9
        </td>
        <td>
            5
        </td>
        <td>
            1
        </td>
    </tr>
    <tr>
        <td>
            2
        </td>
        <td>
            7
        </td>
        <td>
            6
        </td>
    </tr>
</table>

while this one is not:

<table>
    <tr>
        <td>
            3
        </td>
        <td>
            8
        </td>
        <td>
            4
        </td>
    </tr>
    <tr>
        <td>
            5
        </td>
        <td>
            1
        </td>
        <td>
            9
        </td>
    </tr>
    <tr>
        <td>
            7
        </td>
        <td>
            6
        </td>
        <td>
            2
        </td>
    </tr>
</table>

In total, there is only one magic square inside the given grid.

## Example 2:
**Input:** grid = [[8]]

**Output:** 0

## Constraints:
* `row == grid.lenth`
* `col == grid[i].length`
* `1 <= row, col <= 10`
* `0 <= grid[i][j] <= 15`

## Instructions for Running my Solution:
Requires Python 3.10 or higher.

1. Invoke the Python interpreter
2. Import the `solution.py` module
3. Instantiate the module's `Solution` class
4. Invoke the instance's `numMagicSquaresInside` method with a `grid` argument.

## LeetCode Submission Detail:
See here: https://leetcode.com/submissions/detail/1358516768/
