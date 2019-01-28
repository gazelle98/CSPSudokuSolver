# CSP Sudoku Solver

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

In order to eliminate as many contradictory possible values as possible, as quickly as possible, 
this CSP implements the Arc-Consistency: Consistency Propagation algorithm, or AC-3. Whenever a value is 
updated it will form a queue of arcs, which are pairs of positions that are affected by the updated value.
Then it will go through each arc and remove values from the domain of the tail of each arc if they contradict.
If a domain is altered it will add all of the arcs affected by this domain change to the queue and will repeat 
until the queue is empty. 

The possible values of each variable are kept track of in the Sudoku class instances and
when it comes time to decide which variable to expand next in the search, it will use the given
heuristic to determine which variable to expand next. The heuristics that are implemented in this
program are as follows:

- The trivial heuristic.
    - This heuristic returns the first variable that has not yet been expanded.
    - This does not help performance in any way.
- The Minimum Remaining Values (MRV) heuristic.
    - This heuristic chooses the node with the least amount of possible values remaining. 
    - This helps reduce the total number of nodes expanded because there are fewer branches 
    to the search tree this way, and it is more likely to pick the correct value for the given variable.

A state is discarded if it is found to be in violation of any of the constraints of the
sudoku puzzle. If there is more than one of the same number in any given row, column, or 3x3 
sub-square then that state is discarded so that it does not have to keep being expanded until
it is complete to find out that it is incorrect. In addition if a variable's domain is empty, then
that state is discarded because there is no possible value that can be entered there such that the 
state maintains validity.

### Usage
The command line syntax is as follows:

    $ python main.py
    
This command runs the program solving a default easy sudoku problem.

Adding the --help or --h tag to the command line arguments shows a help page for how to initialize this program:

    $python main.py --h
    $python main.py --help

You can add the -sudoku or -s argument followed by easy, medium, hard, hardest, impossible, 
or a the name of a .txt file in the same directory to specify a sudoku to solve.

    $ python main.py -sudoku medium
    $ python main.py -s sudoku.txt

The easy, medium, hard, hardest, and impossible keywords correspond to 5 different built in sudokus of 
varying difficulty that can be used to solve.

If you use he file input option then the program will use the first 81 integers it finds in the .txt file
as the values for the sudoku.

In order to choose which next variable heuristic to use, the -next_var or -nv tag can be added followed
by either trivial, or mrv which correspond to the trivial and minimum remaining values heuristics as explained 
above. The default heuristic is the MRV heuristic.

    $ python main.py -next_var lvp
    $ python main.py -nv trivial