# given an array of integers 'nums', which is sorted in ascending
# order, and an integer 'target', write a function to seach target
# in nums.  if target exists, then return its index.  otherwise
# return -1.  you must write an algorithm with O(logn) runtime 
# complexity

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 
# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = - 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2 # why not just r-l//2? avoid integer overflow, issue for certain problems

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else: # nums[mid] < target: 
                left = mid+1
        return -1

nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target)) # 4

nums2 = [-1,0,3,5,9,12]
target2 = 2
print(Solution().search(nums2, target2)) # -1

# time complexity: O(log(n))

