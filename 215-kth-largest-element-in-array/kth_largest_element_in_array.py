import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
 
        while left <= right:
            choosen_pivot_index = random.randint(left, right)

            final_index_of_chosen_pivot = self.partition(nums, left, right, choosen_pivot_index)

            if final_index_of_chosen_pivot == n - k:
                return nums[final_index_of_chosen_pivot]

            elif final_index_of_chosen_pivot > n - k:
                right = final_index_of_chosen_pivot - 1

            else:
                left = final_index_of_chosen_pivot + 1

        return -1
    def partition(self, nums, left, right, pivot_index):
        pivot_val = nums[pivot_index]
        lesser_items_tail_index = left

        self.swap(nums, pivot_index, right)

        for i in range(left, right):
            if nums[i] < pivot_val:
                self.swap(nums, i, lesser_items_tail_index)
                lesser_items_tail_index += 1

        self.swap(nums, right ,lesser_items_tail_index)

        return lesser_items_tail_index

    def swap(self, nums, first, second):
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp
