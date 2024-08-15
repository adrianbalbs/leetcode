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
