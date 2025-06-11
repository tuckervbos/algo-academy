# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made 
# by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# time complexity: O(m + n) (# nodes in in list1 + list2)
# space complexity: O(1)

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        if list2 == None: return list1

        if list1.val < list2.val:
            next1 = list1.next
            list1.next = self.mergeTwoLists(next1, list2)
            return list1
        else:
            next2 = list2.next
            list2.next = self.mergeTwoLists(list1, next2)
            return list2
        
    def mergeTwoListsIterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # at least one list is now empty
        current.next = list1 if list1 else list2

        return dummy.next
    

# Helper to build a linked list from a list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

# Helper to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Test cases
list1a = build_linked_list([1, 2, 4])
list2a = build_linked_list([1, 3, 4])
result1 = Solution().mergeTwoLists(list1a, list2a)
print("Merged list 1:")
print_linked_list(result1)  # Output: 1 1 2 3 4 4

list1b = build_linked_list([])
list2b = build_linked_list([])
result2 = Solution().mergeTwoLists(list1b, list2b)
print("Merged list 2:")
print_linked_list(result2)  # Output: (prints nothing)

list1c = build_linked_list([])
list2c = build_linked_list([0])
result3 = Solution().mergeTwoLists(list1c, list2c)
print("Merged list 3:")
print_linked_list(result3)  # Output: 0

# Always rebuild lists before reuse
list1a = build_linked_list([1, 2, 4])
list2a = build_linked_list([1, 3, 4])

# Run the test
result1 = Solution().mergeTwoListsIterative(list1a, list2a)
print_linked_list(result1)


