class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]

        def dp(i, count):
            if count < 0:
                return False
            if i == n:
                return count == 0
            if memo[i][count] != -1:
                return memo[i][count] == 1

            is_valid = False
            if s[i] == "*":
                is_valid = (
                    dp(i + 1, count + 1) or dp(i + 1, count - 1) or dp(i + 1, count)
                )
            elif s[i] == "(":
                is_valid = dp(i + 1, count + 1)
            else:  # s[i] == ")"
                is_valid = count > 0 and dp(i + 1, count - 1)

            memo[i][count] = 1 if is_valid else 0
            return is_valid

        return dp(0, 0)

    def checkValidStringTab(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[n][0] = True
        for i in range(n - 1, -1, -1):
            for j in range(n):
                is_valid = False
                if s[i] == "*":
                    is_valid = dp[i + 1][j + 1] or dp[i + 1][j - 1] or dp[i + 1][j]
                elif s[i] == "(":
                    is_valid = dp[i + 1][j + 1]
                else:  # s[i] == ")"
                    is_valid = j > 0 and dp[i + 1][j - 1]
                dp[i][j] = is_valid
        return dp[0][0]
