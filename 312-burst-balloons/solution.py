from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        m = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for i in range(0, n - length):
                j = i + length
                for k in range(i + 1, j):
                    m[i][j] = max(
                        m[i][j], m[i][k] + m[k][j] + nums[i] * nums[k] * nums[j]
                    )
        return m[0][n - 1]
