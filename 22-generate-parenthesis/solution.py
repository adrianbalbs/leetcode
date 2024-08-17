from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parens = []

        def dfs(numOpen, numClosed):
            if numOpen == n and numClosed == n:
                res.append("".join(parens))
                return
            if numOpen < n:
                parens.append("(")
                dfs(numOpen + 1, numClosed)
                parens.pop()

            if numClosed < numOpen:
                parens.append(")")
                dfs(numOpen, numClosed + 1)
                parens.pop()

        dfs(0, 0)
        return res
