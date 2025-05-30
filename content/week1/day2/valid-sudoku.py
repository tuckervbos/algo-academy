# valid-sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
# need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain 
# the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# example 1
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board = list[list[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                curr_val = board[r][c]
                if curr_val != '.':
                    box_coord = f'{r//3},{c//3}' # integer division
                    if curr_val in row[r] or curr_val in col[c] or curr_val in box[box_coord]:
                        return False
                    row[r].add(curr_val)
                    col[c].add(curr_val)
                    box[box_coord].add(curr_val)
        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board)) # True

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board2)) # False

# time complexity:
# space complexity:



# approach notes
# how do we know that a particular cell belongs to a particular box?
# in js, we could use something like Math.floor(r/3)
# in python, just say r//3 (automatic integer division, will just round it down)

# cell (1,7) r//3 = 0 
#            c//3 = 2 (2.33 rounded down)
#            key = 0,2  (this is our key for box hashmap)


# alternate solution from chat
# class Solution(object): 
#     def isValidSudoku(self, board): 
#         res = [] 
#         for i in range(9): 
#             for j in range(9): 
#                 element = board[i][j] 
#                 if element != '.': 
#                     res += [(i, element), (element, j), (i // 3, j // 3, element)] 
#                 return len(res) == len(set(res))