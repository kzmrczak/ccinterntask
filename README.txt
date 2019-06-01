The function is written in Python 3.6
Basically, the task is varied form of the Knapsack problem.
It's one of the most common problem in discrete optimization.
The method that I used is the dynamic programming solution.
So the function takes 2 arguments: size of usb stick ('usb_size') and 
list of memes ('memes'). 

Firstly I calculate 'size_in_mb' because our memes weights are in MiBs, not in GiBs.
Then I create an empty matrix (called 'list') in dim (size_in_mb / the number of memes).

Knapsack problem algorithm go through each column and row of the matrix.
'j' (rows) represents a meme in our list of memes). 
'i' (cols) represents a usb_size

The loop fill first element of each row with 0 (if we have 0 memes size is 0).
Next if the size of meme from previous row is greater than current column number,
cell of 'list' fills up with value from the previous row.
Otherwise cell fills up with Max function.
The Max function compares a: sum of value of meme in caps from previous row and 'list' cell
with coords ([previous row][column - size of meme from previous column]) with value of cell from previous row and 
returns a bigger value.

The last element of the list (in [last row][last column]) is a solution (sum_of_caps).

After that I should also return which values make up the result and add this memes to a set 'chosen memes'.
This for loop iterates trough the last column of solution matrix from the last element to the first.
If value from last column previous row is equal to 'sum_of_caps' it's ignored.
Otherwise 'chosen_memes' append with ith - 1 meme from 'memes' list. The 'max_val_caps' (it has value of 'sum_of_caps')is reduced by
value of that meme, and 'maximum' (it's 'size_in_mb') is reduced by size of this meme.

The result of the function is a tuple with 'sum_of_caps' and 'chosen_memes' set.