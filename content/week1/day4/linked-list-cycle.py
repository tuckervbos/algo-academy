# Given head, the head of a linked list, determine if the 
# linked list has a cycle in it.

# There is a cycle in a linked list if there is some node 
# in the list that can be reached again by continuously 
# following the next pointer. Internally, pos is used to 
# denote the index of the node that tail's next pointer is 
# connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. 
# Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, 
# where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, 
# where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints:
# The number of the nodes in the list is in the range [0, 10^4].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Follow up: Can you solve it using O(1) (i.e. constant) memory?

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None: return False
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False



# Helper to build a linked list and create a cycle at index `pos`
def build_linked_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = []
    for val in values:
        nodes.append(ListNode(val))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]  # create cycle
    return nodes[0]

# Run tests
head1 = build_linked_list_with_cycle([3,2,0,-4], 1)
head2 = build_linked_list_with_cycle([1,2], 0)
head3 = build_linked_list_with_cycle([1], -1)

print("head1 has cycle?", Solution().hasCycle(head1))  # True
print("head2 has cycle?", Solution().hasCycle(head2))  # True
print("head3 has cycle?", Solution().hasCycle(head3))  # False