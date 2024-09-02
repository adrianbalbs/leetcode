from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = [0] * 26
        for c in p:
            p_count[ord(c) - ord("a")] += 1

        left = 0
        anagrams = []
        s_count = [0] * 26
        for right in range(len(s)):
            s_count[ord(s[right]) - ord("a")] += 1
            if right - left + 1 > len(p):
                s_count[ord(s[left]) - ord("a")] -= 1
                left += 1
            if s_count == p_count:
                anagrams.append(left)
        return anagrams
