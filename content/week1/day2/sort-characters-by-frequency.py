# Given a string s, sort it in decreasing order based on the 
# frequency of the characters. The frequency of a character is 
# the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, 
# return any of them.

# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. 
# Therefore "eetr" is also a valid answer.

# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, 
# so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters 
# must be together.

# Example 3:
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" 
# is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 

# Constraints:
# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.


# approach: this screams bucket sort!
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        c = Counter(s) # makes a hash table automatically
        bucket = [[] for _ in range(n+1)]

        for char, freq in c.items():
            bucket[freq].append(char)

        res = ''
        for freq in range(n, 0, -1): # iterate backwards starting from n, to 0, decrementing (-1)
            for char in bucket[freq]:
                res += freq * char
        return res


s1 = "tree"
print(Solution().frequencySort(s1)) # "eert"
s2 = "cccaaa"
print(Solution().frequencySort(s2)) # "aaaccc" || "cccaaa"
s3 = "Aabb"
print(Solution().frequencySort(s3)) # "bbAa"

# time complexity: O(n) because 
# space complexity: O(n + c)