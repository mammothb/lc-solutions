from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(start, n, nums, curr, result):
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                new_curr = curr + [nums[i]]
                result.append(new_curr)
                solve(i + 1, n, nums, new_curr, result)

        nums = sorted(nums)
        result = [[]]
        solve(0, len(nums), nums, [], result)
        return result
