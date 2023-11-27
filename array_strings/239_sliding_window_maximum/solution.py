import collections
import heapq
from typing import Deque, Generic, List, TypeVar

import pytest

T = TypeVar("T")


class MonotonicQueue(Generic[T]):
    def __init__(self) -> None:
        self.queue: Deque = collections.deque()

    def append(self, val: T) -> None:
        # Count is used to track how many element are before the current
        # element in the window
        count = 0
        while self.queue and self.queue[-1][0] < val:
            back = self.queue.pop()
            count += back[1] + 1
        self.queue.append([val, count])

    def max(self) -> T:
        return self.queue[0][0]

    def popleft(self) -> T:
        if self.queue[0][1] > 0:
            self.queue[0][1] -= 1
            return self.queue[0][0]
        else:
            return self.queue.popleft()[0]


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        # Brute force
        result = []
        for i in range(k, len(nums) + 1):
            result.append(max(nums[i - k : i]))
        return result

    def max_sliding_window_heap(self, nums: List[int], k: int) -> List[int]:
        h = [(-num, i) for i, num in enumerate(nums[:k])]
        heapq.heapify(h)
        result = [-h[0][0]]
        i = k
        while i < len(nums):
            heapq.heappush(h, (-nums[i], i))
            # Only trim when the "largest" element is no longer in the window
            while h[0][1] <= i - k:
                heapq.heappop(h)
            result.append(-h[0][0])
            i += 1
        return result

    def max_sliding_window_monotonic(self, nums: List[int], k: int) -> List[int]:
        window: "MonotonicQueue[int]" = MonotonicQueue()
        for i in range(k - 1):
            window.append(nums[i])
        result = []
        i = k - 1
        while i < len(nums):
            window.append(nums[i])
            result.append(window.max())
            window.popleft()
            i += 1
        return result

    def max_sliding_window_monotonic_optimized(
        self, nums: List[int], k: int
    ) -> List[int]:
        window: Deque[int] = collections.deque()
        result = []
        for i, num in enumerate(nums):
            # Keep only the largest element in the window
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            # Remove leftmost element if it moves out of window
            if window[0] == i - k:
                window.popleft()
            if i >= k - 1:
                result.append(nums[window[0]])
        return result


@pytest.mark.parametrize(
    "case,expected",
    [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
        (([1], 1), [1]),
        (([1, -1], 1), [1, -1]),
    ],
)
def test_solution(case, expected):
    nums, k = case
    solution = Solution()

    assert solution.max_sliding_window(nums, k) == expected
    assert solution.max_sliding_window_heap(nums, k) == expected
    assert solution.max_sliding_window_monotonic(nums, k) == expected
    assert solution.max_sliding_window_monotonic_optimized(nums, k) == expected
