from typing import List

import pytest


class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        def search_range(nums, l, r):
            if l >= r and nums[l] != target:
                return -1

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return search_range(nums, l, mid - 1)
            else:
                return search_range(nums, mid + 1, r)

        n = len(nums)
        result = [-1, -1]
        if n == 0:
            return result

        index = search_range(nums, 0, n - 1)
        if index != -1:
            i = index
            j = index
            while i >= 0 and nums[i] == target:
                result[0] = i
                i -= 1

            while j < n and nums[j] == target:
                result[1] = j
                j += 1
        return result

    def search_range_two_bs(self, nums: List[int], target: int) -> List[int]:
        def search_first(nums, n, target):
            l = 0
            r = n - 1
            index = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    index = mid
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return index

        def search_last(nums, n, target):
            l = 0
            r = n - 1
            index = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    index = mid
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return index

        result = [-1, -1]
        n = len(nums)
        if n == 0:
            return result
        result[0] = search_first(nums, n, target)
        if result[0] == -1:
            return result
        result[1] = search_last(nums, n, target)
        return result

    def searchRange_2bs(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]

        start = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    start = mid
                r = mid - 1
            else:
                l = mid + 1
        # Search for last index, set left bound as previous left index
        stop = -1
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                stop = mid
                l = mid + 1
            else:
                r = mid - 1

        return [start, stop]


@pytest.fixture
def solution():
    return Solution()


def test_solution(solution):
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    expected = [3, 4]

    assert solution.search_range(nums, target) == expected
    assert solution.search_range_two_bs(nums, target) == expected


def test_solution_not_found(solution):
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    expected = [-1, -1]

    assert solution.search_range(nums, target) == expected
    assert solution.search_range_two_bs(nums, target) == expected


def test_solution_empty_input(solution):
    nums = []
    target = 0
    expected = [-1, -1]

    assert solution.search_range(nums, target) == expected
    assert solution.search_range_two_bs(nums, target) == expected
