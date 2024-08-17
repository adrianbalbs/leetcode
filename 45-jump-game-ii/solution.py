from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        currEnd = 0
        farthest = 0
        jumps = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currEnd:
                jumps += 1
                currEnd = farthest

            if currEnd >= len(nums) - 1:
                break
        return jumps


test = Solution()
print(test.jump([2, 3, 1, 1, 4]))
print(test.jump([2, 3, 0, 1, 4]))
print(test.jump([1]))
