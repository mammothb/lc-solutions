import heapq
from typing import List


class Solution:
    def largest_sum_after_k_negations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k > 0:
            # use all k attempts on 0 if it's the smallest value
            if nums[0] == 0:
                break
            heapq.heapreplace(nums, -nums[0])
        return sum(nums)
