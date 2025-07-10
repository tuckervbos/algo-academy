# Given n pairs of parentheses, write a function to generate all 
# combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]
 
# Constraints:
# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def _backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                _backtrack(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                _backtrack(openN, closedN+1)
                stack.pop()

        _backtrack(0,0)
        return res
    

# weird time complexity: 4^n / (n * sqrt(n))
# don't need to know this, just that it is exponential and ineficcient 


    
if __name__ == "__main__":
    s = Solution()
    
    # Test Case 1
    n = 1
    expected = ["()"]
    output = s.generateParenthesis(n)
    assert sorted(output) == sorted(expected), f"Test case 1 failed: got {output}"

    # Test Case 2
    n = 3
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    output = s.generateParenthesis(n)
    assert sorted(output) == sorted(expected), f"Test case 2 failed: got {output}"

    # Test Case 3
    n = 2
    expected = ["(())", "()()"]
    output = s.generateParenthesis(n)
    assert sorted(output) == sorted(expected), f"Test case 3 failed: got {output}"

    print("All test cases passed!")