# algo academy week 1 - day 5 - heaps

## heaps / priority queues

### what is a heap / priority queue?

- terms 'heap' & 'priority queue' are interchangeable
- partially ordered data structure
- instead of 'first in first out,' we want to pop out an element by priority
  - we can prioritize either the min val or max val
- properties of min heap
  - structure
    - complete binary tree
      - complete means that we fill out the tree from top to bottom, left to right
    - order property
- because a heap is a complete binary tree, we can actually represent it using an array

### heap implementation

- max heap

- leftChild = 2\*i + 1
- rightChild = 2\*i + 2
- parent = Math.floor((i-1)/2)

### operations of max heap

- poll

  - pop out top element
  - move last element to top
  - heapify down: recursively compare children, swap with bigger child

- push

  - insert element at the end
  - heapify up: recursively swap it with parent, if parent is larger

- heapify

  - in order to convert a set of values to a heap, we would need to push each of the values one by one into the heap

### runtimes

- push: O(log(n))
- poll: O(log(n))
- heapify: O(n)
- peek: O(1)
- search: O(n)

### demos

- last stone weight
-
