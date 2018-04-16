"""

Description:
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

Rows:



There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in to complete the row.

Columns:



There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the column.

Regions



A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region.

Valid board example:



For those who don't know the game, here are some information about rules and how to play Sudoku: http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/

"""


def _check(row):
    return len(set(row)) == 9


def extract_columns(rows):
    cols = []
    flat = [item for sublist in rows for item in sublist]
    for i in range(9):
        cols.append([])
        for j in range(i, len(flat), 9):
            cols[i].append(flat[j])

    return cols


def _append_grid(grids, board,  row_start, row_end, col_start, col_end):
    grids.append([])
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            grids[len(grids) - 1].append(board[i][j])


def extract_grids(board):
    grids = []
    _append_grid(grids, board, 0, 3, 0, 3)
    _append_grid(grids, board, 0, 3, 3, 6)
    _append_grid(grids, board, 0, 3, 6, 9)

    _append_grid(grids, board, 3, 6, 0, 3)
    _append_grid(grids, board, 3, 6, 3, 6)
    _append_grid(grids, board, 3, 6, 6, 9)

    _append_grid(grids, board, 6, 9, 0, 3)
    _append_grid(grids, board, 6, 9, 3, 6)
    _append_grid(grids, board, 6, 9, 6, 9)

    return grids


TRUE = "Finished!"
FALSE = "Try again!"


def done_or_not(board):

    for row in board:
        if not _check(row):
            return FALSE

    for col in extract_columns(board):
        if not _check(col):
            return FALSE

    for grid in extract_grids(board):
        if not _check(grid):
            return FALSE

    return TRUE
