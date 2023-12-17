from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Since 0 and n-1 are linked, our choices are either rob
        # 0 ... n-2 or 1 ... n-1
        n = len(nums)
        if n == 1:
            return nums[0]

        # Rob 0...n-2
        dp = [-1] * n
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, n - 1):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        # Rob 1...n-1
        dp_2 = [-1] * n
        dp_2[0] = 0
        dp_2[1] = nums[1]
        for i in range(1, n - 1):
            dp_2[i + 1] = max(dp_2[i], dp_2[i - 1] + nums[i + 1])
        return max(dp[-1], dp_2[-1])
