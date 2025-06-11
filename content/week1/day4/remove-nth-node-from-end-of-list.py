# Given the head of a linked list, remove the nth node 
# from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
 
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz           # n will not exceed the length

# Follow up: Could you do this in one pass?

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = fast = head

        for i in range(n):
            fast = fast.next

        if not fast:  # if the head is the nth node from the end...
            return head.next 
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head




# Simple print function
def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Test cases
print("Test 1:")
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result1 = Solution().removeNthFromEnd(head1, 2)
print_linked_list(result1)  # Expected: 1 2 3 5

print("Test 2:")
head2 = ListNode(1)
result2 = Solution().removeNthFromEnd(head2, 1)
print_linked_list(result2)  # Expected: (empty output)

print("Test 3:")
head3 = ListNode(1, ListNode(2))
result3 = Solution().removeNthFromEnd(head3, 1)
print_linked_list(result3)  # Expected: 1

print("Test 4:")
head4 = ListNode(1, ListNode(2, ListNode(3)))
result4 = Solution().removeNthFromEnd(head4, 3)
print_linked_list(result4)  # Expected: 2 3