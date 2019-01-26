# CSPSudokuSolver

This is a program that solves sudoku puzzles using artificial intelligence concepts. 
This program treats the puzzle as a Constraint Satisfaction Problem (CSP). Each of the squares in the 
puzzle is treated as a separate variable, with domain 1-9. The constraints to the problem
are that each row, column, and 3x3 sub-square must contain the numbers 1 through 9 with
no repeats.

The way this problem is solved is using the Backtracking Search algorithm. This is a variation
on Depth First Search (DFS) that eliminates states that are invalid before they are expanded to 
completion in order to save time. Also the different variables are expanded in an order
such that it will limit the number of nodes that have to be expanded.

THe possible values of each variable are kept track of in the Sudoku class instances and
when it comes time to decide which variable to expand next in the search, it will choose 
the variable with the least number of possible values left. This helps reduce the total 
number of nodes expanded because there are fewer branches to the search tree this way, and 
it is more likely to pick the correct value for the given variable.

A state is discarded if it is found to be in violation of any of the constraints of the
sudoku puzzle. If there is more than one of the same number in any given row, column, or 3x3 
sub-square then that state is discarded so that it does not have to keep being expanded until
it is complete to find out that it is incorrect.