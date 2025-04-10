# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# 3 scenarios: 
#    1: partial overlap => change end
#    2: no overlap => push
#    3: complete overlap => do nothing

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort()
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_int = {
                'start': intervals[i][0],
                'end': intervals[i][1]
            }

            last_int = {
                'start':  stack[-1][0], 
                'end': stack[-1][1]
            }

            if curr_int['start'] <= last_int['end'] and curr_int['end'] > last_int['end']:
                stack[-1][1] = curr_int['end']
            elif curr_int['start'] > last_int['end']:
                stack.append(intervals[i])
            
        return stack

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals)) # [[1, 6], [8, 10], [15, 18]]






# class Solution:
#     def merge(self, intervals: list[list[int]]) -> list[list[int]]:
#         # sort the intervals based on the start time
#         intervals.sort(key=lambda x: x[0])
        
#         merged = []
        
#         for interval in intervals:
#             # if merged is empty or there is no overlap, append the interval
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#                 # there is an overlap, merge the intervals by updating the end time
#                 merged[-1][1] = max(merged[-1][1], interval[1])
        
#         return merged