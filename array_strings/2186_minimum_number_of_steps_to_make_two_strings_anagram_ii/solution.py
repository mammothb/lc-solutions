from collections import Counter

import pytest


class Solution:
    def min_steps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)

        result = 0
        for c_s, cnt_s in counter_s.items():
            if c_s not in counter_t:
                result += cnt_s
            else:
                result += abs(cnt_s - counter_t[c_s])
        for c_t, cnt_t in counter_t.items():
            if c_t not in counter_s:
                result += cnt_t
        return result


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        (("leetcode", "coats"), 7),
        (("night", "thing"), 0),
    ],
)
def test_solution(solution, case, expected):
    s, t = case
    assert solution.min_steps(s, t) == expected
