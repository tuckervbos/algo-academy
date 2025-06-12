# You are given the root of a binary search tree (BST) 
# and an integer val. 
# Find the node in the BST that the node's value equals val 
# and return the subtree rooted with that node. 
# If such a node does not exist, return null.

# Example 1:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

# Example 2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 10^7
# root is a binary search tree.
# 1 <= val <= 10^7

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        if val < root.val:
            # search left
            return self.searchBST(root.left, val)
        elif val > root.val:
            # search right
            return self.searchBST(root.right, val)
        else:
            return root
        


# Helper to print a subtree as a list in preorder (for simple output)
def print_subtree_preorder(node):
    if not node:
        return
    print(node.val, end=" ")
    print_subtree_preorder(node.left)
    print_subtree_preorder(node.right)

# Test 1: Search for an existing value in the BST
print("Test 1:")
# Tree:        4
#             / \
#            2   7
#           / \
#          1   3
root1 = TreeNode(4,
         TreeNode(2, TreeNode(1), TreeNode(3)),
         TreeNode(7)
)
result1 = Solution().searchBST(root1, 2)
print_subtree_preorder(result1)  # Expected: 2 1 3
print()

# Test 2: Search for a value not in the BST
print("Test 2:")
result2 = Solution().searchBST(root1, 5)
print(result2)  # Expected: None

# Test 3: Search for root value
print("Test 3:")
result3 = Solution().searchBST(root1, 4)
print_subtree_preorder(result3)  # Expected: 4 2 1 3 7
print()

# Test 4: Tree with one node, value exists
print("Test 4:")
root4 = TreeNode(10)
result4 = Solution().searchBST(root4, 10)
print_subtree_preorder(result4)  # Expected: 10
print()

# Test 5: Tree with one node, value doesn't exist
print("Test 5:")
result5 = Solution().searchBST(root4, 5)
print(result5)  # Expected: None