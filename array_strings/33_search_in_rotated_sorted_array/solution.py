from typing import List

import pytest


class Solution:
    #  def search(self, nums: List[int], target: int) -> int:
    #      def binary_search(nums, l, r, target):
    #          while l <= r:
    #              mid = (l + r) // 2
    #              if nums[mid] == target:
    #                  return mid
    #              if nums[mid] < target:
    #                  l = mid + 1
    #              else:
    #                  r = mid - 1
    #          return -1
    #
    #      # Find the start of the rotated pivot
    #      n = len(nums)
    #      l = 0
    #      r = n - 1
    #      while l <= r:
    #          mid = (l + r) // 2
    #          if nums[mid] > nums[-1]:
    #              l = mid + 1
    #          else:
    #              r = mid - 1
    #      start = l
    #      if target <= nums[-1]:
    #          l = start
    #          r = n - 1
    #      else:
    #          l = 0
    #          r = start - 1
    #      return binary_search(nums, l, r, target)

    def search_logn(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        # binary search for start of rotated array
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1

        # l is the start of the 2nd half
        if target <= nums[-1]:
            r = n - 1
        else:
            r = l - 1
            l = 0

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

    def search_one_pass(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        (([1], 0), -1),
    ],
)
def test_solution(solution, case, expected):
    nums, target = case
    assert solution.search(nums, target) == expected
    assert solution.search_logn(nums, target) == expected
