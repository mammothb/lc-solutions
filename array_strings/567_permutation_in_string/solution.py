import collections

import pytest


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        n_1 = len(s1)
        counter_1 = collections.Counter(s1)
        match = 0
        for i, c in enumerate(s2):
            if c in counter_1:
                counter_1[c] -= 1
                match += 1
            if i >= n_1 and s2[i - n_1] in counter_1:
                counter_1[s2[i - n_1]] += 1
                match -= 1
            if match == n_1 and all(v == 0 for v in counter_1.values()):
                return True
        return False


@pytest.mark.parametrize(
    "case,expected",
    [
        (("ab", "eidbaooo"), True),
        (("ab", "eidboaoo"), False),
    ],
)
def test_solution(case, expected):
    s1, s2 = case
    solution = Solution()

    assert solution.check_inclusion(s1, s2) == expected
