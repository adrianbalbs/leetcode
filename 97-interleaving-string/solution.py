class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def solve(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and solve(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and solve(i, j + 1):
                return True

            dp[(i, j)] = False
            return dp[(i, j)]

        return solve(0, 0) if len(s1) + len(s2) == len(s3) else False

    def isInterleaveTab(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[n][m] = True
        for i in range(len(dp) - 1, -1, -1):
            for j in range(len(dp[i]) - 1, -1, -1):
                if (i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]) or (
                    j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]
                ):
                    dp[i][j] = True
        return dp[0][0]
