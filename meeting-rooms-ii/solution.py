from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for i in intervals:
            times.append((i.start, 1))
            times.append((i.end, -1))

        times.sort(key=lambda i: (i[0], i[1]))

        count = 0
        max_count = 0
        for t in times:
            count += t[1]
            max_count = max(max_count, count)
        return max_count
