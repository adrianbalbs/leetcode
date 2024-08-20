from typing import List
import heapq

INF = 1000000


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(1, n + 1)}
        for edge in times:
            adjList[edge[0]].append((edge[1], edge[2]))

        processed = [False] * (n + 1)
        dist = [INF] * (n + 1)
        dist[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            _, v = heapq.heappop(pq)
            if processed[v]:
                continue
            processed[v] = True
            for w, t in adjList[v]:
                if dist[v] + t < dist[w]:
                    dist[w] = dist[v] + t
                    heapq.heappush(pq, (dist[w], w))
        ans = max(dist[1:])

        return ans if ans != INF else -1


test = Solution()
print(test.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(test.networkDelayTime([[1, 2, 1]], 2, 2))
