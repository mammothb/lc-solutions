from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        def find_next_non_overlap(events, n, index):
            l = index + 1
            r = n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if events[index][1] < events[mid][0]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        events = sorted(events, key=lambda x: x[0])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            index = find_next_non_overlap(events, n, i)
            for j in range(1, k + 1):
                dp[i][j] = max(
                    dp[i + 1][j],
                    dp[index][j - 1] + events[i][2],
                )
        return dp[0][-1]
