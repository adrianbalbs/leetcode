from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by ending time to always delete by max ending time
        intervals.sort(key=lambda x: x[1])
        res = 0
        prev = 0
        for i in range(1, len(intervals)):
            if intervals[prev][1] <= intervals[i][0]:
                prev = i
            else:
                res += 1
        return res
