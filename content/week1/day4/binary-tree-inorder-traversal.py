# Given the root of a binary tree, return the inorder traversal
# of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Explanation:

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]
# Explanation:

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 
# Follow up: Recursive solution is trivial,
# could you do it iteratively?

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root: return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right




# Simple test cases
print("Test 1:")
# Tree: 1 → \ → 2 → / → 3
root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(Solution().inorderTraversal(root1))  # Expected: [1, 3, 2]

print("Test 2:")
# Tree: [1,2,3,4,5,null,8,null,null,6,7,9]
root2 = TreeNode(1,
    TreeNode(2,
        TreeNode(4),
        TreeNode(5, TreeNode(6), TreeNode(7))
    ),
    TreeNode(3, None, TreeNode(8, TreeNode(9)))
)
print(Solution().inorderTraversal(root2))  # Expected: [4, 2, 6, 5, 7, 1, 3, 9, 8]

print("Test 3:")
root3 = None
print(Solution().inorderTraversal(root3))  # Expected: []

print("Test 4:")
root4 = TreeNode(1)
print(Solution().inorderTraversal(root4))  # Expected: [1]