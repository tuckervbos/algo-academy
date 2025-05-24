# two-sum
#
# given an array of integers nums and an integer target, return 
# indices of the two numbers such that they add up to target
#
# you may assume that each input would have exactly one solution,
# and you may not use the same element twice
# 
# you can return the answer in any order 
#
# example 1:
# input: nums = [2,7,11,15], target = 9
# output: [0,1]
# explanation: because nums[0] + nums[1] == 9, we return [0,1]
#
# example 2:
# input: nums = [3,2,4] target = 6
# output: [1,2]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash:
                return [i, hash[complement]]
            hash[num] = i

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, ))

