# You are given an m x n integer matrix matrix with 
# the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer 
#   of the previous row.
# Given an integer target, return true if target is in matrix 
#   or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 
#   target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 
#   target = 13
# Output: false
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        top, bottom = 0, rows-1

        while top <= bottom:
            row = top + (bottom - top)//2

            if target > matrix[row][cols-1]:
                top = row+1
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                break

        if top > bottom: 
                return False
            
        row = top + (bottom - top)//2
        left, right = 0, cols-1
        
        while left <= right:
            mid = left + (right-left)//2

            if target > matrix[row][mid]:
                left = mid+1
            elif target < matrix[row][mid]:
                right = mid-1
            else:
                return True
        
        return False
                




matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target)) # true

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(Solution().searchMatrix(matrix2, target2)) # false

