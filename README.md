# CSPSudokuSolver

### Overview
This is a program that solves sudoku puzzles using artificial intelligence concepts. 
This program treats the puzzle as a Constraint Satisfaction Problem (CSP). Each of the squares in the 
puzzle is treated as a separate variable, with domain 1-9. The constraints to the problem
are that each row, column, and 3x3 sub-square must contain the numbers 1 through 9 with
no repeats.

The way this problem is solved is using the Backtracking Search algorithm. This is a variation
on Depth First Search (DFS) that eliminates states that are invalid before they are expanded to 
completion in order to reduce the number of expanded nodes and therefore increase performance. 
Also the different variables are expanded in an order such that it will limit the number 
of nodes that have to be expanded.

THe possible values of each variable are kept track of in the Sudoku class instances and
when it comes time to decide which variable to expand next in the search, it will choose 
the variable with the least number of possible values left. This helps reduce the total 
number of nodes expanded because there are fewer branches to the search tree this way, and 
it is more likely to pick the correct value for the given variable.

A state is discarded if it is found to be in violation of any of the constraints of the
sudoku puzzle. If there is more than one of the same number in any given row, column, or 3x3 
sub-square then that state is discarded so that it does not have to keep being expanded until
it is complete to find out that it is incorrect.

### Usage
The command line syntax is as follows:

    $ python main.py
    
This command runs the program solving a default easy sudoku problem.

Adding the --help or --h tag to the command line arguments shows a help page for how to initialize this program:

    $python main.py --h
    $python main.py --help

You can add the -sudoku or -s argument followed by easy, medium, hard, hardest, or a the name of a .txt file
in the same directory to specify a sudoku to solve.

Examples:

    $ python main.py -sudoku medium
    $ python main.py -s sudoku.txt

The easy, medium, hard, and hardest keywords correspond to 4 different built in sudokus of varying difficulty
that can be used to solve.

If you use he file input option then the program will use the first 81 integers it finds in the .txt file
as the values for the sudoku.