# algo academy - week 1 - day 2 - sorting algorithms

## sorting algorithms

### bubble sort

```
def bubble_sort(nums):
    len = len(nums)
    for i in range(len):
        for j in range(len):
            if nums[j] > nums[j+1]
                let tmp = nums[i]
                nums[i] = nums[i+1]
                nums[j+1] = tmp
    return nums
```

- runtime: O(n^2)
- [visualization](https://visualgo.net/en/sorting)
- this sorting algorithm scans through the array several times, taking in the number and placing it onto the end (over and over until eventually it's sorted)
- this algorithm is highly inefficient, and you would never want to sort this way unless specifically asked to

### merge sort

- [demo](https://leetcode.com/problems/sort-an-array)

```^
        3 2 4 1     || n = 4    |               - notice how size of n is divided
         /    \                 |               - by 2 at each stage of stack:
     3 2       4 1  || n - 2    | log(n) depth
     /  \      / \              |               - that means stack is log(n) deep
    3    2    4   1 || n = 1    |               - so we are doing n work log(n) times
                                                - thats how we get n*log(n)
```

- runtime: O(n\*log(n))
- [visualization](https://visualgo.net/en/sorting)
- this algorithm splits an array in half continuously and then returns sorted halves
- sounds a lot like recursion...

### quick sort

- runtime:
  - worst case: O(n^2)
  - amortized: (n\*log(n))
- unlike merge sort which uses a temp array to merge,
- quicksort can sort IN PLACE with no extra memory

- this algorithm selects a pivot then partitions all values into
- "lesser" and "greater" buckets. it does this until there is only
- one element at most in either the lesser or greater sides and then
- concatenates them with the pivot

- note: this solution will not pass all test cases
- in order to better optimize, we need to select randomized pivots instead

```
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]
        def quickSort(nums, start, end):
            if end-start+1 <= 1: return nums

            pivot = nums[end]
            left = start

            for i in range(start, end+1):
                if nums[i] < pivot:
                    tmp = nums[left]
                    nums[left] = nums[i]
                    nums[i] = tmp
                    left += 1

            nums[end] = nums[left]
            nums[left] = pivot

            quickSort(nums, start, left-1)
            quickSort(nums, left+1, end)

            return nums

        start = 0
        end = len(nums)-1

        return quickSort(nums, start, end)
```

### bucket sort

- runtime: O(n)
- ONLY ALLOWED UNDER CONSTRAINTS
  - we must guarantee that all values fit within a finite range
- as we iterate through the array, we can simply increment a value in an array
- problems:
  - sort colors
  - sort an array (implement merge sort)
  - sort characters by frequency
  - top k frequent elements (bonus)
