# algo academy - week 1 - day 4 - trees

## trees

### binary tree structure and definitions

- similar to linked lists, trees are made of nodes with pointers
  - instead of next or previous pointers, we have left and right
- relationship between connected nodes is a 'parent-child' relationship
- node without a child is considered a 'leaf node'
  - binary trees are always guaranteed to have leaf nodes
  - leaf nodes are very good places to look when it comes to base cases in recursive functions
- node without a parent is considered the 'root' of the binary tree
- if a node is a child or any other node beneath the children, it is considered a 'descendant' of another node
- the height of a node is how far it is from leaf nodes
- the depth of a node is how far it is from root node

### requirements for a binary tree

- has at most one root node
- each node has at most two children
- each node has at most one parent
- a binary tree cannot be cyclic

### binary tree structure

- measuring a binary tree:
  - some prefer to measure height and depth starting from 0 instead of 1
  - some also prefer to measure by edges instead of notes
  - make sure you always define how you're making these measurements to avoid confusion

### tree node in code:

```javascript
class TreeNode(val) {
    this.val = val;
    this.left = null;
    this.right = null;
}
```

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

### binary search trees (BST)

- a few additional properties to binary trees
  - every node on the left subtree must be less than the root value
  - every node on the right subtree must be greater than the root value
  - BSTs generally do not contain duplicates
  - the above properties are recursive, which means they apply to every subtree and not just the root node
- why would a bst be useful?
  - we can use binary search to search the tree... duh
  - can search in O(logn) time complexity
- demo: [search in a binary search tree](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)

###
