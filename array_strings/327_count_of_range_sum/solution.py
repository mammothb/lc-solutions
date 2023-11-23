from typing import List

import pytest


class Solution:
    def count_range_sum(self, nums: List[int], lower: int, upper: int) -> int:
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)

        def merge_sort(sums, start, stop, lower, upper):
            if stop - start <= 1:
                return 0
            mid = (start + stop) // 2
            count = merge_sort(sums, start, mid, lower, upper) + merge_sort(
                sums, mid, stop, lower, upper
            )
            l = mid
            r = mid
            for i in range(start, mid):
                while l < stop and sums[l] - sums[i] < lower:
                    l += 1
                while r < stop and sums[r] - sums[i] <= upper:
                    r += 1
                count += r - l
            sums[start:stop] = sorted(sums[start:stop])
            return count

        return merge_sort(sums, 0, len(sums), lower, upper)


@pytest.fixture
def solution():
    return Solution()


def test_solution(solution):
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    expected = 3

    assert solution.count_range_sum(nums, lower, upper) == expected
