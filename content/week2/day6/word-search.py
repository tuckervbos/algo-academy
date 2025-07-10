# Given an m x n grid of characters board and a string word, 
# return true if word exists in the grid.

# The word can be constructed from letters of sequentially
# adjacent cells, where adjacent cells are horizontally or 
# vertically neighboring. The same letter cell may not be 
# used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],
#                 ["S","F","C","S"],
#                 ["A","D","E","E"]], 
#        word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],
#                 ["S","F","C","S"],
#                 ["A","D","E","E"]], 
#        word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],
#                 ["S","F","C","S"],
#                 ["A","D","E","E"]], 
#        word = "ABCB"
# Output: false

# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 
# Follow up: Could you use search pruning to make your solution faster 
# with a larger board?

# base cases:
#   1) if we find the word, return true
#       a) keep track of index, done when i == len(word)
#   2) False
#       a) out of bounds
#       b) letter does not match with word[i]
#       c) we have visited 

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def _backtrack(r, c, i):
            if i == len(word):
                return True
            if not _inbound(r,c) or word[i] != board[r][c] or (r, c) in visited:
                return False
            
            # modifying
            visited.add((r, c))

            # recursion
            res = (_backtrack(r+1, c, i+1) or
                _backtrack(r-1, c, i+1) or
                _backtrack(r, c+1, i+1) or
                _backtrack(r, c-1, i+1))

            # backtrack
            visited.discard((r,c))

            return res

        def _inbound(r, c):
            rowInBound = r >= 0 and r < ROWS
            colInBound = c >= 0 and c < COLS
            return rowInBound and colInBound

        for r in range(ROWS):
            for c in range(COLS):
                if _backtrack(r, c, 0):
                    return True

        return False
    




if __name__ == "__main__":
    s = Solution()

    # Test Case 1: Word exists in a simple path
    board1 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word1 = "ABCCED"
    assert s.exist(board1, word1) == True, "Test case 1 failed"

    # Test Case 2: Word exists in a vertical/horizontal zigzag
    word2 = "SEE"
    assert s.exist(board1, word2) == True, "Test case 2 failed"

    # Test Case 3: Word requires revisiting a letter (invalid)
    word3 = "ABCB"
    assert s.exist(board1, word3) == False, "Test case 3 failed"

    # Test Case 4: Word is a single letter present
    board2 = [["A"]]
    word4 = "A"
    assert s.exist(board2, word4) == True, "Test case 4 failed"

    # Test Case 5: Word is a single letter not present
    word5 = "B"
    assert s.exist(board2, word5) == False, "Test case 5 failed"

    # Test Case 6: Word uses all cells in a valid path
    board3 = [["A", "B"],
              ["C", "D"]]
    word6 = "ABDC"
    assert s.exist(board3, word6) == True, "Test case 6 failed"

    print("All test cases passed!")