from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            backtrack(i, total + candidates[i], cur)
            cur.pop()
            backtrack(i + 1, total, cur)

        backtrack(0, 0, [])
        return res
