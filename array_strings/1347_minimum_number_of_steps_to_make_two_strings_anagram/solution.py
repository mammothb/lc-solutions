from collections import Counter
from typing import Dict

import pytest


class Solution:
    def min_steps(self, s: str, t: str) -> int:
        counter_s: Dict[str, int] = {}
        counter_t: Dict[str, int] = {}
        for c_s, c_t in zip(s, t):
            if c_s in counter_s:
                counter_s[c_s] += 1
            else:
                counter_s[c_s] = 1
            if c_t in counter_t:
                counter_t[c_t] += 1
            else:
                counter_t[c_t] = 1
        result = 0
        for c_s, cnt_s in counter_s.items():
            if c_s not in counter_t:
                result += cnt_s
            elif cnt_s > (cnt_t := counter_t[c_s]):
                result += cnt_s - cnt_t
        return result

    def min_steps_builtin_counter(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        result = 0
        for c_s, cnt_s in counter_s.items():
            if c_s not in counter_t:
                result += cnt_s
            elif cnt_s > (cnt_t := counter_t[c_s]):
                result += cnt_s - cnt_t
        return result


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        (("bab", "aba"), 1),
        (("leetcode", "practice"), 5),
        (("anagram", "mangaar"), 0),
    ],
)
def test_solution(solution, case, expected):
    s, t = case
    assert solution.min_steps(s, t) == expected
    assert solution.min_steps_builtin_counter(s, t) == expected
