# sort-colors

# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, 
# and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
 
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

# approach: 
# if limited to a few options, usually a good indicator for using bucket-sort

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        do not return anything, modify nums in-place instead
        """
        counts = [0] * 3 # [0, 0, 0]

        for n in nums:
            counts[n] += 1

        i = 0
        for n in range(len(counts)):
            for c in range(counts[n]):
                nums[i] = n
                i += 1

nums = [2,0,2,1,1,0]
print(Solution().sortColors(nums)) # None (no return)
print(nums) #  [0,0,1,1,2,2]

nums2 = [2,0,1]
print(Solution().sortColors(nums2)) # None (no return)
print(nums2) #  [0,1,2]

# Loop                            Style                                 Purpose
# for n in nums                   Loop over values in nums              Count how many of each number (color)
# for n in range(len(counts))     Loop over indexes 0, 1, 2             Know which number we’re rewriting (0s, 1s, 2s)
# for c in range(counts[n])       Loop for each occurrence of number n  Write that number the correct number of times
