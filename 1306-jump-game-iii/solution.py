from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [False] * n

        def dfs(cur):
            if cur < 0 or cur >= n or vis[cur]:
                return False
            if arr[cur] == 0:
                return True
            vis[cur] = True
            return dfs(cur + arr[cur]) or dfs(cur - arr[cur])

        return dfs(start)
