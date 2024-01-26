from typing import List


class Solution:
    def canCross_dp(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][1] = True

        for i in range(1, n):
            for j in range(i):
                k = stones[i] - stones[j]
                if k >= n or not dp[j][k]:
                    continue
                if i == n - 1:
                    return True
                dp[i][k] = True
                if k - 1 >= 0:
                    dp[i][k - 1] = True
                if k + 1 < n:
                    dp[i][k + 1] = True

        return False

    def canCross(self, stones: List[int]) -> bool:
        self.memo = set()
        target = stones[-1]
        stones = set(stones)
        result = self.solve(stones, 1, 1, target)
        return result

    def solve(self, stones, curr, step, target):
        if (curr, step) in self.memo:
            return False

        if curr == target:
            return True
        if curr > target or curr not in stones:
            return False

        for next_step in (step - 1, step, step + 1):
            # Avoid moving backward or not moving
            if step <= 0:
                continue
            curr += next_step
            if curr in stones:
                if self.solve(stones, curr, next_step, target):
                    return True
            curr -= next_step
        self.memo.add((curr, step))
        return False
