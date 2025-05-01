# Arrays

### array metaphor

- librarian responsible for organizing vast collection of books
- imagine an array as shelf on the bookshelf, each slot on the shelf holds a book.
- just like how you easily find a book on a specific shelf if you know what slot it is in,
- you can find a specific element in an array if you know its index
- organize books by categories, could have an array for history, science, etc
- make it easy for peopel to find books they need, and for you to keep track
- just as librarian uses shelves and slots to organize books,
- programmers use arrays to organize collections of values

### static arrays

- fixed size: cannot change

### dynamic arrays

- when a limit is reached, new array copied
- 2x size, small array placed into beginning
- O(1) time (amortized time complexity, 99% of the time)

### array operations

1. read/write ith element: O(1) constant
2. insert/remove end: O(1) constant <- amortized
3. insert middle or beginning: O(n) linear
4. remove middle or beginning: O(n) linear

### recap: data structure

- arrays must be contiguous in memory
- static arrays have a fixed size
- dynamic arrays solve our space problem if we fill up the array with values
  - and are the default for many languages like js/py
- whenever dynamic array needs to be resized when adding new elements: O(n)
  - however, amortized time complexity is O(1)
- read/write ith | insert/remove end ==> O(1)
- insert middle/beginning | remove middle/beginning ==> O(n)

### stacks

- LIFO (last in first out)
- arrays are very efficient when used for stacks
- operations
  - push: O(1)
  - pop: O(1)
  - peek: O(1)

### when should we use a stack

- when we want to ensure system does not move onto another action before completing those before
- when we want to do something in reverse order
- when we want to implement an undo/redo feature
- when we want to backtrack in searching algos (eg path finding in a maze)
- when we use recursion; it utilizes the call stack
