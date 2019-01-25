import sudoku_CSP
import sudoku_problem


def backtracking_search(csp):
    """
    Initializes a backtracking search algorithm to solve the given CSP.

    Keyword arguments:
    csp -- an instance of a SudokuCSP problem used as the problem to be solved.
    """
    assignment = sudoku_problem.Sudoku(csp.get_initial_state())
    return recursive_backtracking(assignment, csp)


def recursive_backtracking(assignment, csp):
    """
    A recursive backtracking search algorithm that uses the given assignment and CSP to solve.

    Keyword arguments:
    assignment -- an instance of a Sudoku representing the assignments to each entry in a CSP.
    csp -- an instance of a SudokuCSP problem used as the problem to be solved.
    """
    if csp.is_complete_assignment(assignment):
        return assignment

    var_pos = csp.get_next_variable(assignment)

    for asgn in csp.get_successors(assignment, var_pos):
        try:
            result = recursive_backtracking(asgn, csp)
            return result
        except ValueError as err:
            if str(err) == "Search Failure.":
                continue
            else:
                raise

    raise ValueError("Search Failure.")
