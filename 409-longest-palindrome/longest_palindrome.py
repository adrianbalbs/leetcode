import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = collections.Counter()
        for c in s:
            charCount[c] += 1

        foundOdd = False
        maxLength = 0
        for count in charCount.values():
            if count % 2 == 1:
                if foundOdd:
                    maxLength += count - 1
                else:
                    maxLength += count
                    foundOdd = True
            else:
                maxLength += count


        return maxLength

solution = Solution()
print(solution.longestPalindrome("abccccdd"))
