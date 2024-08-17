import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for point in points:
            heapq.heappush(heap, (self.distance(point), point))

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    def distance(self, point):
        return math.sqrt(point[0]**2 + point[1]**2)

solution = Solution()

print(solution.kClosest([[1,3], [-2,2]], 1))
