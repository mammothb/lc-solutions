from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        dp = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
            result += dp[i]
        return result

    def numberOfArithmeticSlices_constant_space(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        dp = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
            else:
                dp = 0
            result += dp
        return result
