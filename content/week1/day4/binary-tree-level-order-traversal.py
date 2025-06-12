# Given the root of a binary tree, return the level order traversal 
# of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []
 
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque()
        queue.append(root)
        output = []
        while queue:
            queueLen = len(queue)
            level = []
            for i in range(queueLen):
            # shift out from queue
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                output.append(level)
        return output
    


# Helper to build trees manually
def test_level_order():
    sol = Solution()

    # Test 1: root = [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print("Test 1:", sol.levelOrder(root1))  # Expected: [[3],[9,20],[15,7]]

    # Test 2: root = [1]
    root2 = TreeNode(1)
    print("Test 2:", sol.levelOrder(root2))  # Expected: [[1]]

    # Test 3: root = []
    root3 = None
    print("Test 3:", sol.levelOrder(root3))  # Expected: []

    # Test 4: root = [1, 2, 3, 4, None, None, 5]
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.right.right = TreeNode(5)
    print("Test 4:", sol.levelOrder(root4))  # Expected: [[1], [2, 3], [4, 5]]

test_level_order()