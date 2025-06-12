# Given the roots of two binary trees p and q, write a function 
# to check if they are the same or not.

# Two binary trees are considered the same if they are structurally 
# identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 
# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4

# approach
# 1) both null, return true
# 2) both same val, return true
# 3) one null other not null, return false
# 4) 

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    



# Test cases
print("Test 1:")
# Tree p:      1
#             / \
#            2   3
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().isSameTree(p1, q1))  # Expected: True

print("Test 2:")
# Tree p:      1
#             / 
#            2   
# Tree q:      1
#               \
#                2
p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
print(Solution().isSameTree(p2, q2))  # Expected: False

print("Test 3:")
# Tree p:      1
#             / \
#            2   1
# Tree q:      1
#             / \
#            1   2
p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))
print(Solution().isSameTree(p3, q3))  # Expected: False

print("Test 4:")
# Both are None
p4 = None
q4 = None
print(Solution().isSameTree(p4, q4))  # Expected: True

print("Test 5:")
# One is None, one is not
p5 = TreeNode(1)
q5 = None
print(Solution().isSameTree(p5, q5))  # Expected: False