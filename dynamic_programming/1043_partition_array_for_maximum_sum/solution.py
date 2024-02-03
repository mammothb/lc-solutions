from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            curr_max = float("-inf")
            for j in range(1, k + 1):
                if i - j >= 0:
                    curr_max = max(curr_max, arr[i - j])
                    dp[i] = max(dp[i], dp[i - j] + curr_max * j)
        return dp[-1]

    def maxSumAfterPartitioning_memoization(self, arr: List[int], k: int) -> int:
        n = len(arr)
        self.dp = [0] * n
        return self.solve(arr, k, 0, n)

    def solve(self, arr, k, start, stop):
        if start >= stop:
            return 0
        if self.dp[start] != 0:
            return self.dp[start]
        max_elem = 0
        max_sum = 0
        for i in range(k):
            if start + i >= stop:
                continue
            max_elem = max(max_elem, arr[start + i])
            max_sum = max(
                max_sum, max_elem * (i + 1) + self.solve(arr, k, start + i + 1, stop)
            )
        self.dp[start] = max_sum
        return self.dp[start]
