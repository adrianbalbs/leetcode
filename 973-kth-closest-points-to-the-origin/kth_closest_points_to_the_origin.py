import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSelect(points, k, 0, len(points) - 1)

    def quickSelect(self, points: List[List[int]], k, left, right):
        pivotIndex = random.randint(left, right)
        chosenPivot = self.partition(points, left, right, pivotIndex)

        if chosenPivot == k - 1:
            return points[:chosenPivot + 1]
        elif chosenPivot > k - 1:
            return self.quickSelect(points, k, left, chosenPivot - 1)
        else:
            return self.quickSelect(points, k, chosenPivot + 1, right)

    def partition(self, points: List[List[int]], left, right, pivotIndex):
        pivotValue = points[pivotIndex]
        j = left
        points[right], points[pivotIndex] = points[pivotIndex], points[right]

        for i in range(left, right):
            if self.distance(points[i]) < self.distance(pivotValue):
                points[i], points[j] = points[j], points[i]
                j += 1

        points[j], points[right] = points[right], points[j]
        return j

    def distance(self, point):
        return point[0]**2 + point[1]**2

solution = Solution()

print(solution.kClosest([[1,3], [-2,2]], 1))
