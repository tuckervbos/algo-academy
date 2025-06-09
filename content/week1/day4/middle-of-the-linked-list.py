# Given the head of a singly linked list, return the middle node 
# of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

from typing import Optional

# definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head # same as slow = head, fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
# Manually create: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = Solution().middleNode(head)

# Print from middle to end
while result:
    print(result.val, end=" ")
    result = result.next
print()  # → prints: 3 4 5

# Another test: 1 -> 2 -> 3 -> 4 -> 5 -> 6
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
result2 = Solution().middleNode(head2)
while result2:
    print(result2.val, end=" ")
    result2 = result2.next
print()  # → prints: 4 5 6