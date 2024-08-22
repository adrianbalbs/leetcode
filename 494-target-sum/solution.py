from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        n = len(nums)

        def dp(i, total):
            if i == n:
                return 1 if total == target else 0
            if (i, total) in cache:
                return cache[(i, total)]

            cache[(i, total)] = dp(i + 1, total - nums[i]) + dp(i + 1, total + nums[i])
            return cache[(i, total)]

        return dp(0, 0)
