# Given the root of a binary tree, return the postorder 
# traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Explanation:

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]
# Explanation:

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

# Constraints:
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 
# Follow up: Recursive solution is trivial, 
# could you do it iteratively?

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root: return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right

print("Preorder Test 1:")
root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(Solution().preorderTraversal(root1))  # Expected: [1, 2, 3]

print("Preorder Test 2:")
root2 = TreeNode(1,
    TreeNode(2,
        TreeNode(4),
        TreeNode(5, TreeNode(6), TreeNode(7))
    ),
    TreeNode(3, None, TreeNode(8, TreeNode(9)))
)
print(Solution().preorderTraversal(root2))  # Expected: [1, 2, 4, 5, 6, 7, 3, 8, 9]
