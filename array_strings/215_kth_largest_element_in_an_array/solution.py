import heapq
import random
from typing import List

import pytest


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)
        return heap[0]

    def find_kth_largest_quick_select(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            index = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
            nums[index], nums[r] = nums[r], nums[index]
            return index

        n = len(nums)
        l = 0
        r = n - 1

        while True:
            pivot_index = random.randint(l, r)
            new_pivot_index = partition(nums, l, r, pivot_index)
            if new_pivot_index == n - k:
                return nums[new_pivot_index]

            if new_pivot_index < n - k:
                l = new_pivot_index + 1
            else:
                r = new_pivot_index - 1

    def findKthLargest_quick_select_desc(self, nums: List[int], k: int) -> int:
        def quick_select(nums, l, r, k):
            if l == r:
                return nums[l]

            pivot = random.randint(l, r)
            pivot = partition(nums, l, r, pivot)
            if pivot == k - 1:
                return nums[pivot]
            if k - 1 < pivot:
                r = pivot - 1
            else:
                l = pivot + 1
            return quick_select(nums, l, r, k)

        def partition(nums, l, r, pivot):
            nums[pivot], nums[r] = nums[r], nums[pivot]
            idx = l
            for i in range(l, r):
                if nums[i] >= nums[r]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    idx += 1
            nums[idx], nums[r] = nums[r], nums[idx]
            return idx

        return quick_select(nums, 0, len(nums) - 1, k)


print(Solution().findKthLargest_qs([3, 2, 1, 5, 6, 4], 2))


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        (([3, 2, 1, 5, 6, 4], 2), 5),
        (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    ],
)
def test_solution(solution, case, expected):
    nums, k = case

    assert solution.find_kth_largest(nums, k) == expected

    nums, k = case
    assert solution.find_kth_largest_quick_select(nums, k) == expected
