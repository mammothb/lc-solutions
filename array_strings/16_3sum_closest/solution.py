from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        result = float("inf")

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == target:
                    return curr

                if abs(curr - target) < abs(result - target):
                    result = curr

                if curr > target:
                    r -= 1
                else:
                    l += 1
        return result
