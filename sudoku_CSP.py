class SudokuCSP:
    def __init__(self, initial_sudoku):
        """
        Initializes an instance of a SudokuCSP.

        Keyword arguments:
        initial_sudoku -- an instance of a Sudoku object representing the initial state of the sudoku to be solved.
        """
        self.initial_sudoku = initial_sudoku

    def get_initial_state(self):
        """
        Gets the initial state of this sudoku csp problem.

        Returns the initial state by calling the get_state() method on the initial_sudoku of this csp.
        """
        self.initial_sudoku.get_state()
