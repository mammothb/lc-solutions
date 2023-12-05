import pytest


class Solution:
    def switch(self, target: str) -> int:
        last = "0"
        count = 0
        for c in target:
            if c != last:
                last = c
                count += 1
        return count


@pytest.mark.parametrize(
    "case,expected", [("10111", 3), ("101", 3), ("00000", 0), ("001011101", 5)]
)
def test_solution(case, expected):
    solution = Solution()
    assert solution.switch(case) == expected
