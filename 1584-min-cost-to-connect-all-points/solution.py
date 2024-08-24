from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points[i + 1 :], start=i + 1):
                distances.append([i, j, self.manhattanDist(p1, p2)])

        self.parent = [i for i in range(len(points))]
        self.size = [1] * len(points)

        distances.sort(key=lambda x: x[2])
        min_cost = 0
        for i, j, dist in distances:
            if self.find_set(i) != self.find_set(j):
                min_cost += dist
                self.union_set(i, j)
        return min_cost

    def manhattanDist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def find_set(self, v: int) -> int:
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_set(self, a: int, b: int) -> None:
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.size[a] < self.size[b]:
                b, a = a, b
            self.parent[b] = a
            self.size[a] += self.size[b]

    def minCostConnectPointsPrim(self, points: List[List[int]]) -> int:
        n = len(points)
        min_cost = 0
        visited = [False] * n
        min_heap = [(0, 0)]

        edges_used = 0

        while edges_used < n:
            cost, i = heapq.heappop(min_heap)

            if visited[i]:
                continue

            visited[i] = True
            min_cost += cost
            edges_used += 1

            for j in range(n):
                if not visited[j]:
                    dist = abs(points[i][0] - points[j][0]) + abs(
                        points[i][1] - points[j][1]
                    )
                    heapq.heappush(min_heap, (dist, j))

        return min_cost
