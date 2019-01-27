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


def arc_consistency_3(assignment, initial_arcs):
    """
    This is an implementation of the ac-3 arc consistency: constraint propagation algorithm.

    This algorithm removes all of the inconsistent possible values in the assignment in order to reduce the number
    of possibilities, and in turn increase efficiency by reducing the number of nodes to expand.

    Keyword arguments:
    assignment -- an instance of a Sudoku representing the assignments to each entry in a CSP.
    """
    arc_queue = initial_arcs

    while len(arc_queue) > 0:
        head, tail = arc_queue.pop(0)
        if remove_inconsistent_values(assignment, head, tail) and len(assignment.get_possible_values(tail[0], tail[1])) == 1:
            for pos in assignment.get_neighbors(tail[0], tail[1]):
                arc_queue.append((tail, pos))


def remove_inconsistent_values(assignment, head, tail):
    """
    Removes inconsistent values from the tail that do not agree with values in the head.

    Returns a boolean indicating whether any values were removed.

    Keyword arguments:
    assignment -- an instance of a Sudoku representing the assignments to each entry in a CSP.
    head -- a tuple containing the row and column of the head of the consistency arc to be evaluated.
    tail -- a tuple containing the row and column of the tail of the consistency arc to be evaluated.
    """
    removed = False

    hr, hc = head
    tr, tc = tail
    #
    # same_row = hr == tr
    # same_col = hc == tc
    #
    # hsr = hr // 3
    # hsc = hc // 3
    # tsr = tr // 3
    # tsc = tc // 3
    #
    # same_square = hsr == tsr and hsc == tsc
    #
    # in_conflict = same_row or same_col or same_square

    possible_tail_values = list(assignment.get_possible_values(tr, tc))
    possible_head_values = assignment.get_possible_values(hr, hc)

    if len(possible_head_values) == 1 and (possible_head_values[0] in possible_tail_values) and assignment.get_entry(tr, tc) == 0:
        possible_tail_values.remove(possible_head_values[0])
        removed = True
        print(str(hr), str(hc), str(tr), str(tc), str(possible_head_values), str(possible_tail_values), str(assignment.get_entry(tr, tc)))

    # for ptv in list(possible_tail_values):
    #     allowed = False
    #     for phv in possible_head_values:
    #         if ptv != phv or not in_conflict:
    #             allowed = True
    #             break
    #
    #     if not allowed:
    #         possible_tail_values.remove(ptv)
    #         removed = True

    assignment.set_possible_values(tr, tc, possible_tail_values)
    return removed
