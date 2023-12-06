import collections
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def solve(nums, result, curr):
            if sum(nums.values()) == 0:
                result.append(curr)
                return
            for n in nums:
                if nums[n] > 0:
                    nums[n] -= 1
                    solve(nums, result, curr + [n])
                    nums[n] += 1
            # for i in range(len(nums)):
            #     if i > 0 and nums[i] == nums[i - 1]:
            #         continue
            #     solve(nums[:i] + nums[i + 1:], result, curr + [nums[i]])

        result = []
        solve(collections.Counter(nums), result, [])
        return result
