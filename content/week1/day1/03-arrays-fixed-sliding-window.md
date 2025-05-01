# Arrays II

## fixed sliding window

- typically the sliding window has left and right pointers to represent the boundaries of the window
- we can keep track of contents of a window using a hash table or set
- the aim of the sliding window is to reduce the need of nested loops and instead replace it with a single loop
  - can effectively reduce time complexity from O(n2) to O(n)
- this is useful when we want to find subarrays or substrings that meet a given condition within a given length
- example: contains duplicate II
