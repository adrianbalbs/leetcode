class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialise an array of size n + 1 to store counts
        # Base cases dp[0] = 0, dp[1] = 1
        dp = [1 for _ in range(n + 1)]

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


soln = Solution()
print(soln.climbStairs(4))
