from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        dp = [1] * n

        idx = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[idx] < dp[i]:
                idx = i

        i = idx
        count = dp[idx]
        result = []
        while i >= 0:
            if nums[idx] % nums[i] == 0 and dp[i] == count:
                result.append(nums[i])
                idx = i
                count -= 1
            else:
                i -= 1
        return result
