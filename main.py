import sudoku_CSP
import sudoku_problem
import search
import time
import sys

# Solution found in 1834 node expansions with trivial next_variable heuristic and no inferences
# Solution found in 200 node expansions with just partially optimized next variable heuristic
# Solution found in 84 node expansions with optimized next variable
# Solution found in 57 node expansions with optimized next variable and ac-3
easy_sudoku_state = [[0, 5, 3, 0, 0, 0, 7, 9, 0],
                     [0, 0, 9, 7, 8, 2, 6, 0, 0],
                     [0, 0, 0, 5, 0, 3, 0, 0, 0],
                     [0, 0, 0, 4, 0, 6, 0, 0, 0],
                     [0, 4, 0, 0, 0, 0, 0, 6, 0],
                     [8, 0, 5, 1, 0, 9, 3, 0, 2],
                     [0, 0, 8, 9, 3, 1, 4, 0, 0],
                     [9, 0, 0, 0, 0, 0, 0, 0, 6],
                     [0, 0, 4, 0, 0, 0, 8, 0, 0]]

# Solution found in 287,637 node expansions with trivial next_variable heuristic and no inferences
# Solution found in 606 node expansions with just partially optimized next variable heuristic
# Solution found in 54 node expansions with optimized next variable heuristic
# Solution found in 54 node expansions with optimized next variable heuristic and ac-3
medium_sudoku_state = [[0, 0, 0, 0, 0, 0, 0, 9, 0],
                       [0, 5, 0, 0, 0, 0, 2, 0, 1],
                       [0, 0, 0, 0, 0, 7, 6, 0, 0],
                       [0, 0, 0, 0, 4, 1, 5, 0, 0],
                       [0, 0, 0, 6, 0, 0, 0, 0, 9],
                       [0, 0, 6, 2, 0, 0, 4, 0, 7],
                       [0, 7, 3, 1, 0, 6, 0, 0, 5],
                       [9, 0, 0, 0, 0, 0, 0, 0, 2],
                       [0, 4, 0, 0, 7, 9, 3, 8, 0]]

# Solution found in 752 node expansions with just partially optimized next variable heuristic
# Solution found in 80 node expansions with optimized next variable heuristic
# Solution found in 55 node expansions with optimized next variable heuristic and ac-3
hard_sudoku_state = [[2, 0, 5, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [8, 0, 0, 0, 9, 0, 7, 2, 0],
                     [7, 0, 1, 5, 2, 0, 0, 0, 8],
                     [0, 0, 0, 0, 0, 0, 9, 0, 0],
                     [4, 0, 6, 9, 1, 0, 0, 0, 3],
                     [1, 0, 0, 0, 8, 0, 4, 6, 0],
                     [0, 0, 0, 0, 0, 0, 5, 0, 0],
                     [9, 0, 7, 4, 0, 0, 0, 0, 0]]


# Solution found in 10,101 node expansions with optimized next variable heuristic
# Solution found in 2444 node expansions with optimized next variable heuristic and ac-3
worlds_hardest_sudoku_state = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 3, 6, 0, 0, 0, 0, 0],
                               [0, 7, 0, 0, 9, 0, 2, 0, 0],
                               [0, 5, 0, 0, 0, 7, 0, 0, 0],
                               [0, 0, 0, 0, 4, 5, 7, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0, 3, 0],
                               [0, 0, 1, 0, 0, 0, 0, 6, 8],
                               [0, 0, 8, 5, 0, 0, 0, 1, 0],
                               [0, 9, 0, 0, 0, 0, 4, 0, 0]]


def parse_sudoku(sudoku_str):
    """
    Parses a string into a representation of a sudoku state as a 9x9 list of integers.

    Keyword arguments:
    str -- a string consisting of 81 integers between 0 and 9 representing the values of the entries of a sudoku.
    """
    sudoku = [[0 for x in range(9)] for y in range(9)]
    counter = 0
    for char in sudoku_str:
        if counter > 80:
            break

        try:
            val = int(char)
            row = counter // 9
            col = counter % 9
            sudoku[row][col] = val
            counter += 1
        except ValueError:
            continue

    if counter < 80:
        raise ValueError("Not enough integer values in sudoku string input.")
    else:
        return sudoku


def print_initial_and_solution(init_state, sol_state):
    """
    Prints the given initial and solution state of a sudoku side by side.

    Keyword arguments:
    init_state -- a 9x9 list of lists of integers representing the starting state of the solution
    sol_state -- a 9x9 list of lists of integers representing the solution state of the solution
    """
    output_string = "\nInitial state:             Solution state:\n"
    for row in range(9):
        for init_col in range(9):
            output_string += str(init_state[row][init_col]) + " "

        output_string += " " * 9

        for sol_col in range(9):
            output_string += str(sol_state[row][sol_col]) + " "

        output_string += "\n"

    print(output_string)


def main():
    """
    Runs the program using the given command line arguments as input.

    The command line syntax is as follows:
        $ python main.py
    This command runs the program solving a default easy sudoku problem.

    Adding the --help or --h tag to the command line arguments shows a
    help page for how to initialize this program:
        $python main.py --h

    You can add the -sudoku or -s argument followed by easy, medium,
    hard, hardest, or a the name of a .txt file in the same directory
    to specify a sudoku to solve.

    Examples:
        $ python main.py -sudoku medium
        $ python main.py -s sudoku.txt

    The easy, medium, hard, and hardest keywords correspond to 4 different
    built in sudokus of varying difficulty that can be used to solve.

    If you use he file input option then the program will use the first 81
    digits it finds in the .txt file as the values for the sudoku."""
    sudoku_state = easy_sudoku_state
    sudoku_dict = {"easy": easy_sudoku_state,
                   "medium": medium_sudoku_state,
                   "hard": hard_sudoku_state,
                   "hardest": worlds_hardest_sudoku_state}

    for i, arg in enumerate(sys.argv):
        if arg == "--help" or arg == "--h":
            print("\n" + "-" * 75),
            print(main.__doc__)
            print("-" * 75 + "\n")
            sys.exit(0)
        if arg == "-sudoku" or arg == "-s":
            if sys.argv[i + 1] in sudoku_dict:
                sudoku_state = sudoku_dict[sys.argv[i + 1]]
            else:
                try:
                    sudoku_file = open(sys.argv[i + 1], "r")
                    sudoku_state = parse_sudoku(sudoku_file.read())
                except FileNotFoundError:
                    raise ValueError("Given argument for sudoku input \"-s\" is invalid.")

    initial_sudoku = sudoku_problem.Sudoku(sudoku_state)
    csp = sudoku_CSP.SudokuCSP(initial_sudoku)

    start = time.clock()
    solution = search.backtracking_search(csp)
    end = time.clock()

    print_initial_and_solution(sudoku_state, solution.get_state())

    print("Time elapsed: " + str(end - start) + " seconds.")
    print("Number of nodes expanded: " + str(csp.get_num_expanded()) + "\n")


if __name__ == "__main__":
    main()
