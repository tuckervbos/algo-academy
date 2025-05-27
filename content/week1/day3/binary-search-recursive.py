class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def recurse(left, right):
            if left >= right:
                return right if nums[right] == target else -1
            pivot = left + (right - left)//2

            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                return recurse(left, pivot-1)
            else: 
                return recurse(pivot + 1, right)
        return recurse(0, len(nums) - 1)
    
nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target)) # 4

nums2 = [-1,0,3,5,9,12]
target2 = 2
print(Solution().search(nums2, target2)) # -1