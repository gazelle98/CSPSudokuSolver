import sudoku_CSP
import sudoku_problem
import search

# Solution found in 1834 node expansions with trivial next_variable method and no inferences
# Solution found in 200 node expansions with just partially optimized next variable
easy_sudoku_state = [[0, 5, 3, 0, 0, 0, 7, 9, 0],
                     [0, 0, 9, 7, 8, 2, 6, 0, 0],
                     [0, 0, 0, 5, 0, 3, 0, 0, 0],
                     [0, 0, 0, 4, 0, 6, 0, 0, 0],
                     [0, 4, 0, 0, 0, 0, 0, 6, 0],
                     [8, 0, 5, 1, 0, 9, 3, 0, 2],
                     [0, 0, 8, 9, 3, 1, 4, 0, 0],
                     [9, 0, 0, 0, 0, 0, 0, 0, 6],
                     [0, 0, 4, 0, 0, 0, 8, 0, 0]]

# Solution found in 287,637 node expansions with trivial next_variable method and no inferences
# Solution found in 606 node expansions with just partially optimized next variable
medium_sudoku_state = [[0, 0, 0, 0, 0, 0, 0, 9, 0],
                       [0, 5, 0, 0, 0, 0, 2, 0, 1],
                       [0, 0, 0, 0, 0, 7, 6, 0, 0],
                       [0, 0, 0, 0, 4, 1, 5, 0, 0],
                       [0, 0, 0, 6, 0, 0, 0, 0, 9],
                       [0, 0, 6, 2, 0, 0, 4, 0, 7],
                       [0, 7, 3, 1, 0, 6, 0, 0, 5],
                       [9, 0, 0, 0, 0, 0, 0, 0, 2],
                       [0, 4, 0, 0, 7, 9, 3, 8, 0]]

# Solution found in 752 node expansions with just partially optimized next variable
hard_sudoku_state = [[2, 0, 5, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [8, 0, 0, 0, 9, 0, 7, 2, 0],
                     [7, 0, 1, 5, 2, 0, 0, 0, 8],
                     [0, 0, 0, 0, 0, 0, 9, 0, 0],
                     [4, 0, 6, 9, 1, 0, 0, 0, 3],
                     [1, 0, 0, 0, 8, 0, 4, 6, 0],
                     [0, 0, 0, 0, 0, 0, 5, 0, 0],
                     [9, 0, 7, 4, 0, 0, 0, 0, 0]]

if __name__ == "__main__":
    initial_sudoku = sudoku_problem.Sudoku(hard_sudoku_state)
    csp = sudoku_CSP.SudokuCSP(initial_sudoku)
    solution = search.backtracking_search(csp)
    solution.print_sudoku()
