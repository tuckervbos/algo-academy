# Given the head of a singly linked list, reverse the list, 
# and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 
# Follow up: A linked list can be reversed either iteratively 
# or recursively. Could you implement both?

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        def _helper(head, prev):
            if head is None:
                return prev
            
            next = head.next
            head.next = prev
            return _helper(next, head)
        return _helper(head, prev)

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next # save next
            curr.next = prev # reverse link
            prev = curr # move prev forward
            curr = next_node # move curr forward
        return prev 

# Manually create linked lists
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head2 = ListNode(1, ListNode(2))
head3 = None  # empty list

# Helper to print list from any node
def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Run tests
print("Reversed head1:")
print_linked_list(Solution().reverseList(head1))  # Output: 5 4 3 2 1

print("Reversed head2:")
print_linked_list(Solution().reverseList(head2))  # Output: 2 1

print("Reversed head3:")
print_linked_list(Solution().reverseList(head3))  # Output: (prints nothing)