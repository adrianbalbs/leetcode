from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSum = -math.inf
        currSum = 0
        for n in nums:
            currSum = max(n, currSum + n)
            bestSum = max(bestSum, currSum)
        return int(bestSum)
