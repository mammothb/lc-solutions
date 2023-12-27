import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = [(num_list[0], i, 0) for i, num_list in enumerate(nums)]
        heapq.heapify(h)
        right = max(num_list[0] for num_list in nums)

        result = [float("-inf"), float("inf")]
        while h:
            left, i, j = heapq.heappop(h)
            if right - left < result[1] - result[0]:
                result = [left, right]

            if j + 1 == len(nums[i]):
                return result

            right = max(right, nums[i][j + 1])
            heapq.heappush(h, (nums[i][j + 1], i, j + 1))
        return result
