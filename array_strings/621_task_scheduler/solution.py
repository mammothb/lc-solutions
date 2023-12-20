import collections
import heapq
from typing import Dict, List

import pytest


class Solution:
    def least_interval(self, tasks: List[str], n: int) -> int:
        """
        Case 1: 3A, 2B, 1C, n=2
            Start with A__A__A. Idle partition count is count(A) - 1. Each
            partition is size n.
        Case 2: 3A, 2B, 2C, 2D, 2E, n=2
            Start with A__A__A. Realize idle slots between A is **minimum** n.
            ABCDEABCDEA is a valid schedule. So after if len(tasks) > min
            valid duration, just return len(tasks)
        """
        counter = collections.Counter(tasks)
        max_count = max(counter.values())
        result = (max_count - 1) * (n + 1)
        for count in counter.values():
            if count == max_count:
                result += 1
        return max(len(tasks), result)

    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        num_max = 0
        max_count = 0
        for task in counter:
            if counter[task] > max_count:
                max_count = counter[task]
                num_max = 1
            elif counter[task] == max_count:
                num_max += 1
        result = (max_count - 1) * (n + 1) + 1 + num_max - 1
        return max(result, len(tasks))

    def least_interval_priority_queue(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        counter = collections.Counter(tasks)
        h = [-count for count in counter.values()]
        # Process the task with the largest amount left
        heapq.heapify(h)

        cooldown: Dict[int, int] = {}
        curr_time = 0
        while h or cooldown:
            cd_up_idx = curr_time - n - 1
            # if task cooldown is up, add it back to queue to be processed
            if cd_up_idx in cooldown:
                heapq.heappush(h, -cooldown.pop(cd_up_idx))
            if h:
                remaining_count = -heapq.heappop(h) - 1
                # Current task still unfinished, add to cooldown
                if remaining_count > 0:
                    cooldown[curr_time] = remaining_count
            curr_time += 1
        return curr_time


@pytest.mark.parametrize(
    "case,expected",
    [
        ((["A", "A", "A", "B", "B", "B"], 2), 8),
        ((["A", "A", "A", "B", "B", "B"], 0), 6),
        ((["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2), 16),
    ],
)
def test_solution(case, expected):
    tasks, n = case
    solution = Solution()

    assert solution.least_interval(tasks, n) == expected
    assert solution.least_interval_priority_queue(tasks, n) == expected
