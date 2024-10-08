from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        i = 0
        r = len(nums) - 1
        while i <= r:
            if nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                continue
            elif nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            i += 1
