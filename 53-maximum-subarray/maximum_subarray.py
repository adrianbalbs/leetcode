class Solution:
    def maxSubArray(self, nums: "list[int]") -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(max, dp[i])
        return res
            
solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))