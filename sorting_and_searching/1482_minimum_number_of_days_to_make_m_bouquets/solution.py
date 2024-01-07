from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        if m * k == n:
            return max(bloomDay)

        min_day = min(bloomDay)
        max_day = max(bloomDay)
        while min_day <= max_day:
            mid_day = min_day + (max_day - min_day) // 2
            count = 0
            num_bouquet = 0
            for day in bloomDay:
                if day <= mid_day:
                    count += 1
                else:
                    count = 0
                if count == k:
                    num_bouquet += 1
                    count = 0

            if num_bouquet >= m:
                max_day = mid_day - 1
            else:
                min_day = mid_day + 1
        return min_day
