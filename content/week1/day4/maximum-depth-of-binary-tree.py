# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along 
# the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2
 
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    



# Helper to run test cases
def test_max_depth():
    sol = Solution()

    # Test 1: root = [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print("Test 1:", sol.maxDepth(root1))  # Expected: 3

    # Test 2: root = [1,null,2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print("Test 2:", sol.maxDepth(root2))  # Expected: 2

    # Test 3: root = []
    root3 = None
    print("Test 3:", sol.maxDepth(root3))  # Expected: 0

    # Test 4: root = [1]
    root4 = TreeNode(1)
    print("Test 4:", sol.maxDepth(root4))  # Expected: 1

    # Test 5: root = [1, 2, None, 3]
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    print("Test 5:", sol.maxDepth(root5))  # Expected: 3

test_max_depth()