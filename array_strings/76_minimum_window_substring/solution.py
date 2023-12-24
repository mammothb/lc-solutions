import collections

import pytest


class Solution:
    def min_window(self, s: str, t: str) -> str:
        counter_t = collections.Counter(t)
        n_s = len(s)
        n_matches = len(t)
        window_size = n_s + 1
        min_l = 0
        l = 0
        r = 0
        while r < n_s:
            if s[r] in counter_t:
                counter_t[s[r]] -= 1
                # If the new character is a valid match and not in excess
                if counter_t[s[r]] >= 0:
                    n_matches -= 1
            # current window contains `t`
            while n_matches == 0:
                if r + 1 - l < window_size:
                    window_size = r + 1 - l
                    min_l = l
                if s[l] in counter_t:
                    counter_t[s[l]] += 1
                    # new window no longer contains `t`
                    if counter_t[s[l]] > 0:
                        n_matches += 1
                l += 1
            r += 1
        return "" if window_size > n_s else s[min_l : min_l + window_size]

    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        start = 0
        min_length = float("inf")
        result = ""
        for i, c in enumerate(s):
            if c in counter:
                counter[c] -= 1
            while start < i and (s[start] not in counter or counter[s[start]] < 0):
                if s[start] in counter:
                    counter[s[start]] += 1
                start += 1
            if all(val <= 0 for val in counter.values()):
                if i - start + 1 < min_length:
                    min_length = i - start + 1
                    result = s[start : i + 1]

        return result


@pytest.mark.parametrize(
    "case,expected",
    [
        (("ADOBECODEBANC", "ABC"), "BANC"),
        (("a", "a"), "a"),
        (("a", "aa"), ""),
    ],
)
def test_solution(case, expected):
    s, t = case
    solution = Solution()

    assert solution.min_window(s, t) == expected
