class SudokuCSP:
    def __init__(self, initial_sudoku):
        """
        Initializes an instance of a SudokuCSP.

        Keyword arguments:
        initial_sudoku -- an instance of a Sudoku object representing the initial state of the sudoku to be solved.
        """
        self.initial_sudoku = initial_sudoku
        self.expanded_nodes = 0

    def get_initial_state(self):
        """
        Gets the initial state of this sudoku csp problem.

        Returns the initial state by calling the get_state() method on the initial_sudoku of this csp.
        """
        return self.initial_sudoku.get_state()

    def is_complete_assignment(self, assignment):
        """
        Determines if the given assignment of values to a sudoku is a valid solution to this SudokuCSP.

        Keyword arguments:
        assignment -- an instance of a Sudoku representing the assignments to each entry in this CSP.
        """

        for r in range(0, 9):
            for c in range(0, 9):
                entry = self.initial_sudoku.get_entry(r, c)
                if entry != 0 and entry != assignment.get_entry(r, c):
                    raise ValueError("Assignment does not match initial state values.")

        result = assignment.is_complete() and assignment.is_valid()

        if result:
            print("Number of nodes expanded: " + str(self.expanded_nodes))

        return assignment.is_complete() and assignment.is_valid()

    def get_next_variable(self, assignment):
        """
        Determines the next variable in the assignment to be expanded.

        Returns a tuple containing the row and column of the next variable to be expanded.

        Keyword arguments:
        assignment -- an instance of a Sudoku representing the assignments to each entry in this CSP.
        """

        pos_list = []
        num_possible_list = []
        for r in range(0, 9):
            for c in range(0, 9):
                if assignment.get_entry(r, c) == 0:
                    pos = (r, c)
                    pos_list.append(pos)
                    num_possible_list.append(len(assignment.get_possible_values(r, c)))

        if len(pos_list) > 0:
            return pos_list[num_possible_list.index(min(num_possible_list))]
        else:
            raise ValueError("Assignment is already complete.")

    def get_successors(self, assignment, variable_pos):
        """
        Gets all of the valid successors of the given assignment in regards to the variable position.

        Keyword arguments:
        assignment -- an instance of a Sudoku representing the assignments to each entry in this CSP.
        variable_pos -- a tuple containing the row and column of the variable to be expanded.
        """
        r, c = variable_pos
        if assignment.get_entry(r, c) != 0:
            raise ValueError("Variable position is already filled.")
        else:
            successors = []
            for n in range(1, 10):
                new_state = assignment.deep_copy()
                new_state.set_element(r, c, n)
                if new_state.is_valid():
                    successors.append(new_state)

            self.expanded_nodes += 1
            print(self.expanded_nodes)
            return successors
