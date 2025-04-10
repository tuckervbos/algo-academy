# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        for char in s:
            if char not in mapping:
                stack.append(char)
            elif not stack or stack[-1] != mapping[char]:
                return False
            else:
                stack.pop()
                
        return not stack
    

s = "([])"
print(Solution().isValid(s))