class Sudoku:
    def __init__(self, sudoku):
        """
        Initializes an instance of a Sudoku.

        Keyword arguments:
        sudoku -- a 9 by 9 list of lists representing all of the values in a sudoku problem. The entries in the list
        of lists may either be the numbers 1 to 9 representing the puzzle values at those positions,
        or 0 representing an empty entry.
        """
        self.sudoku = sudoku

    def get_state(self):
        """
        Gets the current state of the sudoku as a copy of the list of lists.
        """
        state = []
        for row in self.sudoku:
            state.append(list(row))

        return state

    def set_element(self, row, col, entry):
        """
        Sets the value at the given row and column values to the given entry value.

        Keyword arguments:
        row -- an integer from 0 to 8 representing the row of the desired entry.
        col -- an integer from 0 to 8 representing the column of the desired entry.
        entry -- an integer from 1 to 9 representing the value to be inserted at the given position
        """
        self.sudoku[row][col] = entry

    def get_entry(self, row, col):
        """
        Gets the entry at the given row and column values from this sudoku problem.

        Keyword arguments:
        row -- an integer from 0 to 8 representing the row of the desired entry.
        col -- an integer from 0 to 8 representing the column of the desired entry.
        """
        return self.sudoku[row][col]

    def get_row(self, row):
        """
        Gets the desired row from this sudoku problem.

        Keyword arguments:
        row -- an integer from 0 to 8 representing the desired row.
        """
        return self.sudoku[row]

    def get_col(self, col):
        """
        Gets the desired column from this sudoku problem.

        Keyword arguments:
        col -- an integer from 0 to 8 representing the desired column.
        """
        column = []
        for i, r in enumerate(self.sudoku):
            column.append(r[col])
        return column

    def get_square(self, square_row, square_col):
        """
        Gets the 3x3 sub-square of this sudoku problem.

        Keyword arguments:
        square_row -- an integer from 0 to 2 representing the row of the desired sub-square.
        square_col -- an integer from 0 to 2 representing the column of the desired sub-square.
        """
        square = []
        initial_row_num = square_row * 3
        initial_col_num = square_col * 3

        for i in range(initial_row_num, initial_row_num + 3):
            square.append(self.sudoku[i][initial_col_num:initial_col_num + 3])

        return square
