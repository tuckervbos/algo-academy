# Given an unsorted array of integers nums, return the length of 
# the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums) # O(n)
        longest = 0
        for n in num_set:
            if (n-1) not in num_set:
                # beginning of sequence
                length = 0
                while (n+length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest

nums = [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums)) # 4

nums2 = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums2)) # 9

nums3 = [1,0,1,2]
print(Solution().longestConsecutive(nums3)) # 3

# O(n)