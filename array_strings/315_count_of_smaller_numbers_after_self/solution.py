from typing import List

import pytest


class Solution:
    def count_smaller(self, nums: List[int]) -> List[int]:
        n_nums = len(nums)
        result = [0] * n_nums

        def merge_sort(arr, start, stop):
            if stop - start <= 1:
                return
            mid = (start + stop) // 2
            merge_sort(arr, start, mid)
            merge_sort(arr, mid, stop)

            l = start
            r = mid
            # number of element on the right array that's smaller than the
            # current left element
            count = 0
            cache = []
            while l < mid and r < stop:
                if arr[l][1] > arr[r][1]:
                    cache.append(arr[r])
                    count += 1
                    r += 1
                else:
                    cache.append(arr[l])
                    result[arr[l][0]] += count
                    l += 1
            while l < mid:
                cache.append(arr[l])
                # all the elements in the right arry were smaller
                result[arr[l][0]] += count
                l += 1
            while r < stop:
                cache.append(arr[r])
                r += 1
            for i, n in enumerate(cache):
                arr[start + i] = n

        merge_sort(list(enumerate(nums)), 0, n_nums)
        return result


def test_solution():
    nums = [5, 2, 6, 1]
    expected = [2, 1, 1, 0]
    solution = Solution()

    assert solution.count_smaller(nums) == expected
