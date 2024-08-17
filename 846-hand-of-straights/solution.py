from collections import Counter, OrderedDict
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = OrderedDict(Counter(sorted(hand)))
        while counts:
            curr = next(iter(counts))
            for i in range(curr, curr + groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    counts.pop(i)
        return True
