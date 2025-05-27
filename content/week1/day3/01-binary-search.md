# algo academy - week 1 - day 3 - binary search

## binary search

### binary search

- binary search is an extremely efficient searching algorithm
- it is one of the few algorithms that can reach O(log(n)) runtime
- prerequisite for binary search is usually to have sorted array
  - however there are some exceptions when you can binary search on things that aren't simply sorted arrays

target = 8
[1, 3, 3, 4, 5, 6, 7, 8]

- look at approx middle number: 4
  - 4 = 8? no
  - 4 < 8? yes
    - eliminate 4-1, leaving 5-8
- look at approx middle number: 6
  - 6 = 8? no
  - 6 < 8? yes
    - eliminate 5-6
- pick middle: 7
  - 7 = 8? no
  - 7 < 8? yes
    - elim 7
- pick middle: 8

  - 8 = 8? YES
    - return index [7]

- binary seach demo
- given an array of integers 'nums' which is sorted in ascending order, and an integer 'target', write a function to search 'target' in 'nums'. if 'target' exists, return its index. otherwise return -1. must write an algorithm with O(logn) runtime complexity.

- iterative solution:

```python
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
```

- recursive solution:

```python
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
```

### searching ranges

- demo: guess number higher or lower
