from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(nums, n, start, length, result, curr):
            if length == 0:
                result.append(curr)
                return
            for i in range(start + 1, n):
                solve(nums, n, i, length - 1, result, curr + [nums[i]])

        result = [[], nums]
        n = len(nums)
        for length in range(1, n):
            for i in range(n):
                solve(nums, n, i, length - 1, result, [nums[i]])

        return result
