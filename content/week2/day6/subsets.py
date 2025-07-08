# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
 
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        subset = []

        def _backtrack(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return
            
            # decision to INCLUDE nums[i]
            subset.append(nums[i])
            _backtrack(i+1)
            subset.pop()

            # decision to NOT INCLUDE nums[i]
            _backtrack(i+1)
            
        _backtrack(0)
        return ans
    



s = Solution()

# Test Case 1: Example from prompt
print(sorted(s.subsets([1, 2, 3])))  
# Expected (order may vary):
# [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

# Test Case 2: Single element
print(sorted(s.subsets([0])))  
# Expected: [[], [0]]