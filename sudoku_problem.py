class Sudoku:
    def __init__(self, sudoku_state):
        """
        Initializes an instance of a Sudoku.

        Keyword arguments:
        sudoku_state -- a 9 by 9 list of lists representing all of the values in a sudoku problem.
        The entries in the list of lists may either be the numbers 1 to 9 representing the puzzle values at
        those positions, or 0 representing an empty entry.
        """
        for row in sudoku_state:
            for entry in row:
                if entry < 0 or entry > 9:
                    raise ValueError("All entries must be 0 to 9.")

        self.sudoku_state = sudoku_state

    def get_state(self):
        """
        Gets the current state of the sudoku as a copy of the list of lists.
        """
        state = []
        for row in self.sudoku_state:
            state.append(list(row))

        return state

    def deep_copy(self):
        """
        Returns a deep copy of this instance of a Sudoku.
        """
        return Sudoku(self.get_state())

    def set_element(self, row, col, entry):
        """
        Sets the value at the given row and column values to the given entry value.

        Keyword arguments:
        row -- an integer from 0 to 8 representing the row of the desired entry.
        col -- an integer from 0 to 8 representing the column of the desired entry.
        entry -- an integer from 1 to 9 representing the value to be inserted at the given position
        """
        if entry < 1 or entry > 9:
            raise ValueError("Entry in sudoku must be between 1 and 9.")
        elif row < 0 or row > 8:
            raise ValueError("Row value must be between 0 and 8")
        elif col < 0 or col > 8:
            raise ValueError("Column value must be between 0 and 8")
        else:
            self.sudoku_state[row][col] = entry

    def get_entry(self, row, col):
        """
        Gets the entry at the given row and column values from this sudoku problem.

        Keyword arguments:
        row -- an integer from 0 to 8 representing the row of the desired entry.
        col -- an integer from 0 to 8 representing the column of the desired entry.
        """
        if row < 0 or row > 8:
            raise ValueError("Row value must be between 0 and 8")
        elif col < 0 or col > 8:
            raise ValueError("Column value must be between 0 and 8")
        else:
            return self.sudoku_state[row][col]

    def get_row(self, row):
        """
        Gets the desired row from this sudoku problem.

        Keyword arguments:
        row -- an integer from 0 to 8 representing the desired row.
        """
        if row < 0 or row > 8:
            raise ValueError("Row value must be between 0 and 8")
        else:
            return self.sudoku_state[row]

    def get_col(self, col):
        """
        Gets the desired column from this sudoku problem.

        Keyword arguments:
        col -- an integer from 0 to 8 representing the desired column.
        """
        if col < 0 or col > 8:
            raise ValueError("Column value must be between 0 and 8")
        else:
            column = []
            for i, r in enumerate(self.sudoku_state):
                column.append(r[col])
            return column

    def get_square(self, square_row, square_col):
        """
        Gets the 3x3 sub-square of this sudoku problem.

        Keyword arguments:
        square_row -- an integer from 0 to 2 representing the row of the desired sub-square.
        square_col -- an integer from 0 to 2 representing the column of the desired sub-square.
        """
        if square_row < 0 or square_row > 2:
            raise ValueError("Square row value must be between 0 and 2")
        elif square_col < 0 or square_col > 2:
            raise ValueError("Square column value must be between 0 and 2")
        else:
            square = []
            initial_row_num = square_row * 3
            initial_col_num = square_col * 3

            for i in range(initial_row_num, initial_row_num + 3):
                square.append(self.sudoku_state[i][initial_col_num:initial_col_num + 3])

            return square

    def get_square_as_list(self, square_row, square_col):
        """
        Gets the 3x3 sub-square of this sudoku problem in the form of a single list.

        Keyword arguments:
        square_row -- an integer from 0 to 2 representing the row of the desired sub-square.
        square_col -- an integer from 0 to 2 representing the column of the desired sub-square.
        """
        square = self.get_square(square_row, square_col)
        square_list = []
        for row in square:
            for entry in row:
                square_list.append(entry)

        return square_list

    def is_complete(self):
        """
        Determines if the state of this Sudoku has no empty entries.
        """
        for row in self.sudoku_state:
            for entry in row:
                if entry == 0:
                    return False

        return True

    def is_valid(self):
        """
        Determines if the current state is not in violation of any of the constraints of a sudoku puzzle.
        """

        for i in range(0, 9):
            for n in range(1, 10):
                if self.get_row(i).count(n) > 1 or self.get_col(i).count(n) > 1:
                    return False

        for sr in range(0, 3):
            for sc in range(0, 3):
                for n in range(1, 10):
                    if self.get_square_as_list(sr, sc).count(n) > 1:
                        return False

        return True

    def print_sudoku(self):
        """
        Prints the state of this sudoku to the output.
        """
        sudoku_string = ""
        for r in range(0, 9):
            for c in range(0, 9):
                sudoku_string += str(self.get_entry(r, c)) + " "
            sudoku_string += "\n"
        print(sudoku_string)
