import collections


# O(n) Space Complexity Solution
class Solution:
    def majorityElement(self, nums: "list[int]") -> int:
        numCount = collections.Counter()
        for i in nums:
            numCount[i] += 1
        return numCount.most_common(1)[0][0]


solution = Solution()
print(solution.majorityElement([2,2,1,1,1,2,2]))
print(solution.majorityElement([3,2,3]))