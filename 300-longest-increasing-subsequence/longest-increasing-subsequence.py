class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                dp[i] = 1
            else:
                max_nums: list[int] = []
                for j in range(i):
                    if nums[j] < nums[i]:
                        max_nums.append(dp[j])
                if max_nums:
                    dp[i] = max(max_nums) + 1
                else:
                    dp[i] += 1
        return max(dp)
