class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # Is the end of the new interval less than the start of the current one
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Is the start of the new interval greater than the end of the current one
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # Merge the intervals together by taking the min of the start points and max of the ending points
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res