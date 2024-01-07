from typing import Dict, List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][diff] represent the number of subsequence that ends with nums[i]
        # of at least size 2
        dp: List[Dict[int, int]] = [{} for _ in range(n)]

        result = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j].get(diff, 0)

                if diff in dp[i]:
                    dp[i][diff] += count + 1
                else:
                    dp[i][diff] = count + 1
                # If there's a subsequence with diff at dp[j], there will be 1
                # more element at dp[i] making it size 3 minimum
                result += count
        return result
