from functools import reduce
import operator
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums, 0)
