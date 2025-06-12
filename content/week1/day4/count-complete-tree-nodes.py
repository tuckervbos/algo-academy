# Given the root of a complete binary tree, return the number 
# of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, 
# is completely filled in a complete binary tree, and all nodes 
# in the last level are as far left as possible. It can have 
# between 1 and 2^h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: 6

# Example 2:
# Input: root = []
# Output: 0

# Example 3:
# Input: root = [1]
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.

# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 1. create a queue initialized with root
        # 2. shift out from queue (current node)
        # 3. process node - increment count
        # 4. push current node's children into queue
        # 5. repeat steps 2-4 until queue is empty 

        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            node = queue.popleft()
            if node: 
                count += 1
                queue.append(node.left)
                queue.append(node.right)
        return count
    
# this is not log(n), just boiler plate for now