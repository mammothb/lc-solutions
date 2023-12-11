from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # Leave offsets at 0 when neighbors elements have the same rating, e.g.,
        # [1, 2, 2] results in [1, 2, 1] candies
        offsets = [0] * n
        # Get offsets where L > R
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                offsets[i] = 1
        # Get offsets where L < R
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                offsets[i] = 1
        # Cumulative sum of L > R, skip if current offset is already larger, e.g.,
        # [3,1,0] results in [3,2,1] candies but has an initial offset of [1,1,0]
        # Also [1,2,3,4,1,0] results in [1,2,3,4,2,1] candies
        for i in range(n - 2, -1, -1):
            if (
                offsets[i] > 0
                and ratings[i] > ratings[i + 1]
                and offsets[i] <= offsets[i + 1]
            ):
                offsets[i] = offsets[i + 1] + 1
        # Cumulative sum of L < R, skip if current offset is already larger
        for i in range(1, n):
            if (
                offsets[i] > 0
                and ratings[i] > ratings[i - 1]
                and offsets[i] <= offsets[i - 1]
            ):
                offsets[i] = offsets[i - 1] + 1

        result = 0
        for offset in offsets:
            result += 1 + offset
        return result

    def candy_two_pass(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1] * n
        # Offsets were modified as arr[i] = 1 + arr[i - 1] instead of
        # arr[i] += 1 + arr[i - 1]
        # Don't have to do a separate loop for it
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                result[i] = 1 + result[i - 1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                if result[i] <= result[i + 1]:
                    result[i] = 1 + result[i + 1]

        return sum(result)
