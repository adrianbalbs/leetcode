class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        count_list = list(count.items())
        k_elems = sorted(count_list, key=lambda key: key[1], reverse=True)[:k]
        res = [res[0] for res in k_elems]
        return res
