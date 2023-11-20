from typing import List

import pytest


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        # fmt: off
        (["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ",
          "c","a","n","a","l",":"," ","P","a","n","a","m","a"],
         ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",",
          "n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]),
        # fmt: on
    ],
)
def test_solution(solution, case, expected):
    solution.reverse_string(case)
    assert case == expected
