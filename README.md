# sudoku_subgrouping
Try to solve a sudoku board via subgrouping. This project attempts to solve a sudoku board using only the concept of subgrouping (when X number of tiles in a group can only be X possible numbers).

## 
To run, input:
```
python SudokuSolver.py --initial_vals [list of starting coords and vals]
```
where a starting coord,val would look like "<x-coord>,<y-coord>,<val>". The x-coordinates go left to right, and y-coordinates go top to bottom, and both are 0-indexed.

For example, an input could look like:
```
python SudokuSolver.py --initial_vals 0,2,9 0,4,7 0,6,4 0,8,3 1,0,1 1,3,2 1,5,4 2,2,5 2,4,1 2,8,7 3,2,3 3,3,1 3,8,5  4,0,5 4,1,8 4,4,3 5,7,9 6,4,8 6,7,2 7,2,2 7,5,7 7,8,9 8,1,6
```
