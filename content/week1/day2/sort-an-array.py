# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions 
# in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers 
# are not changed (for example, 2 and 3), while the positions of other 
# numbers are changed (for example, 1 and 5).

# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 

# Constraints
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) < 2: return nums # base case
        
        mid = len(nums)//2  ## integer division, will "Math.floor()" (round down) for us
        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid::])

        return self.merge(left, right)

    def merge(self, left, right): # python already has a merge method!
        merged = []

        while len(left) and len(right): # must be and, can't be or
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))

        return merged + left + right


nums = [5,2,3,1]
print(Solution().sortArray(nums)) #[1,2,3,5]

nums2 = [5,1,1,2,0,0]
print(Solution().sortArray(nums2))# [0,0,1,1,2,5]
