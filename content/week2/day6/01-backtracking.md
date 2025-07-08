# algo academy week 2 - day 6 - backtracking

## backtracking

### what is backtracking

- backtracking is an algorithmic technique where we solve problems recursively by 'building candidates' for solutions and then abandon those candidates ("backtrack") once we determine that candidate can no longer yield a valid solution
- build on dfs and an optimization of 'exhaustive search,' where we search through all possible candidates
- backtracking is an optimization that involves abandoning a 'path' once it is determined that the path cannot lead to a solution (in other words, our base case)
- this is an important concept because some problems can only be (reasonably) solved via backtracking
- most common type of problem that can be solved with backtracking is 'find all possible ways to do something'
- backtracking problems run in exponential runtime, example: O(2^n) (or 5^N, 10^N, etc)

- [example](01.1-backtracking.png)

### backtracking skeleton

```python
# let curr represent the thing you are building
# it could be an array or a combination of values
def backtrack(curr, OTHER_ARGUMENTS...):
    if("BASE_CASE"):
        # modify the answer
        return

    for ("ITERATE_OVER_INPUT"):
        # modify the current state
        backtrack(curr, OTHER_ARGUMENTS...)
        # undo the modification of the current state
```

### demo

- (subsets)[]
