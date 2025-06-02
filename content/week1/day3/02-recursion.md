# algo academy - week 1 - day 3

## recursion

### recursion

- recursion is a vital concept that must be understood as a prerequisite for many algorithms that we will see moving forward
- linked list problems are a good place to practice recursion due to their simplicity compared to trees or graphs
- recursion inherently creates a stack, specifically the call stack, which works very similarly to a stack created by an array
- all recursion solutions can also be written iteratively, but this can actually overly complicate some problems

### comparing recursive and iterative code

- iterative:

```python
def traverse(head):
    current = head
    while current: # conditional (as long as currnode is not null)
        current = current.next #
    return 0
```

- recursive:

```python
def traverse(head):
    if not head: return 0 # base case (if we reach a null node, return 0 immediately)
    return traverse(head.next)
```

- most important part of recursive fuction is base case. this is the termination point of the function. it is similar to conditionals put in while loops. while loops run till condition is met. recursive functions continue to run until hit base case

### single path demo

- example: reverse linked list

```python
class ListNode:
    def __init__(self, val=0, next=None)
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        def _helper(head, prev):
            if head is None:
                return prev # returns the new head of the newly reversed linked list
            next = head.next # save next before overwritting
            head.next = prev # overwrite/reverse pointer
            return _helper(next, head) # move down the list
        return _helper(head, prev) # recursive call/step
```

### runtime complexity

- single-path recursive functions usually run O(n) where n is depth of stack
- multi-path recursive functions can be analyzed with the following formula: (# of paths)^(depth of stack)
- [runtime-complexity](/content/week1/day3/runtime-complexity.png)
- tree in the above photo represents recursive fibonacci function
- each node has at most 2 branching paths
- depth of stack is 5, which is input
- thus we can call this O(2^n) where n is our input number O(2^5)
- extremely inefficient, only factorial is worse

### drawbacks of exponential runtimes

- exponential runtimes are extremely inefficient
- if you run into exponential runtimes, there is likely a way to reduce the time complexity somehow (we will discuss this much later when we get to dynamic programming)
- unique paths (brute force)
