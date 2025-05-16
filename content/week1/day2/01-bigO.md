# algo academy - week 2 - day 1 = big o notation

## Big O Notation / Analysis

### Big O Analysis

- Big O is how we analyze how efficient our solutions are
- helps us understand how well our solutions work at scale
- two things to analyze: time, space
- generally, we are more concerned with time
  - still important to understand how to analyze space efficiency as well
- we are usually talking about worst case scenario
  - however, there are a few niche cases where we take the average into consideration instead
  - this is called "amortized complexity"
  - inserting elements into dynamic arrays are an example of this

### Big O Rules

- Dropping constants
  - O(2n) is effectively O(n) for large inputs
- dropping non-dominant terms
  - O(n + log(n)) can be simplified to O(n) since O(n) is slower than O(log(n))
- amortized time
  - dynamic array example:
    - arrays must be resized when reaching capacity, which is an O(n) operation
    - however, this doesnt happen often
    - if the vast majority of the time we can expect a O(1) push time complexity, we can amortize the runtime to O(1) even if the worst case scenario is O(n)
- when figuring out complexities, ask yourself: How do my operations scale as my input gets larger?
- always always always define your variables. the correctness of your analysis is dependent on how you define your variables
  - ex: O(n) time where n is number of elements in matrix

### Big O Chart

- O(1)
- O(logn)
- O(n)
- O(nlogn)
- O(n^2)
- O(2^n)
- O(n!)

### O(1) - constant

- O(1) is most optimal time complexity possible
- no matter how our input grows, number of operations remain the same
- represented by a flat line
- remember for small inputs sometimes constant is slower in some cases
- examples:
  - arrays:
    - nums = [1, 2, 3]
    - nums.append(4) // pushing to end of array
    - nums.pop() // popping from end of array
    - nums[0] // lookup
  - hash maps / sets
    - hash = {}
    - hash["key"] = 10 // insert
    - "key" in hash // lookup

### O(n) - linear

- As our input size grows, operations grow proportionally
- note: nested loops can still be O(n) (eg, sliding window)
- examples:
  - arrays:
    - nums = [1, 2, 3]
    - for num in nums // looping
    - 2 in nums // searching
    - nums.pop(0) // removing from beginning (have to reassign all of the indices)

### O(n^2)

- as our input grows, our operations grow quadratically
- examples
  - traversing a _square_ matrix
    - nums = [[1,2,3], [4,5,6], [7,8,9]]
    - for row in range(len(nums)):
      - for col in range(len(nums[0])):
        - print(nums[row][col])
  - get every pair of elements in array
    - nums = [1,2,3]
    - for i in range(len(nums)):
      - for j in range(i + 1, len(nums)):
        - print(nums[i], nums[j])

### O(n \* m)

- just because we have nested loops does not mean O(n^2)!!!
- we must define our variables
- example:
  - traversing a rectangle matrix
    - nums = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    - for row in range(len(nums)):
      - for col in range(len(nums)):
        - print(nums([row][col]))

### O(n^3)

- example:
  - getting triplets of elements in an array
    - for i in range(len(nums)):
      - for j in range(i+1, len(nums)):
        - for k in range(j+1, len(nums)):
          - print(nums[i], nums[j], nums[k])
- probably a better way to do things

### O(log(n)) - logrithmic

- as our input size grows, our operations grow logarithmically
- marginally less efficient than O(1) but much more efficient than O(n)
- examples:
  -     binary search:
        ```
        nums = [1,2,3,4,5], target = 6
        l, r = 0, len(nums) - 1
        while l <= r
            m = (l + r) //2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                print(m)
                break
        ```
    - pushing and popping from heaps:
      - import heapq
      - minHeap = []
      - heapq.heappush(minHeap, 5)
      - heapq.heappop(minHeap)

### O(n \* log(n))

- marginally more inefficient than O(n) but much more efficient than O(n^2)
