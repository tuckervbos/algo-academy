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
