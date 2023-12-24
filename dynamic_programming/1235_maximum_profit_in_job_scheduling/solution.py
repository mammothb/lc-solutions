from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        def find_last_non_overlapping_index(startTime, endTime, index):
            l = 0
            r = index - 1
            while l <= r:
                mid = l + (r - l) // 2
                if endTime[mid] <= startTime[index]:
                    if endTime[mid + 1] <= startTime[index]:
                        l = mid + 1
                    else:
                        return mid
                else:
                    r = mid - 1
            return -1

        startTime, endTime, profit = zip(
            *sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        )

        n = len(profit)
        dp = [0] * n
        dp[0] = profit[0]

        for i in range(1, n):
            include = profit[i]

            index = find_last_non_overlapping_index(startTime, endTime, i)
            if index != -1:
                include += dp[index]
            dp[i] = max(include, dp[i - 1])
        return dp[-1]

    def jobScheduling_2(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        def find_next_non_overlap(startTime, endTime, n, index):
            l = index + 1
            r = n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if endTime[index] <= startTime[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        startTime, endTime, profit = zip(
            *sorted(
                zip(startTime, endTime, profit),
                key=lambda x: x[0],
            )
        )

        n = len(profit)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            index = find_next_non_overlap(startTime, endTime, n, i)
            dp[i] = max(dp[i + 1], dp[index] + profit[i])
        return dp[0]
