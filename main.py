import sudoku_CSP
import sudoku_problem
import search

easy_sudoku_state = [[0, 5, 3, 0, 0, 0, 7, 9, 0],
                     [0, 0, 9, 7, 8, 2, 6, 0, 0],
                     [0, 0, 0, 5, 0, 3, 0, 0, 0],
                     [0, 0, 0, 4, 0, 6, 0, 0, 0],
                     [0, 4, 0, 0, 0, 0, 0, 6, 0],
                     [8, 0, 5, 1, 0, 9, 3, 0, 2],
                     [0, 0, 8, 9, 3, 1, 4, 0, 0],
                     [9, 0, 0, 0, 0, 0, 0, 0, 6],
                     [0, 0, 4, 0, 0, 0, 8, 0, 0]]

if __name__ == "__main__":
    initial_sudoku = sudoku_problem.Sudoku(easy_sudoku_state)
    csp = sudoku_CSP.SudokuCSP(initial_sudoku)
    solution = search.backtracking_search(csp)
    solution.print_soduku()
