from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: index for index, char in enumerate(s)}

        start = 0
        end = 0
        res = []
        for index, char in enumerate(s):
            end = max(end, last[char])
            if index == end:
                res.append(end - start + 1)
                start = end + 1

        return res
