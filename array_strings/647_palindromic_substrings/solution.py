import pytest


class Solution:
    def count_substrings(self, s: str) -> int:
        # Realize that if abcba is a palindrome, so is:
        # bcb (remove 1 char on both sides) and
        # c (remove 1 char on both sides)
        #
        # So we can pick a center and keep expanding until we no longer find
        # a palindrome.
        # l, r are used to account for palindromes with both odd and even number
        # of letters.
        def expand_and_count_palindrome(s, l, r):
            count = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1
            return count

        result = 0
        for i in range(len(s)):
            result += expand_and_count_palindrome(
                s, i, i
            ) + expand_and_count_palindrome(s, i, i + 1)
        return result


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("case,expected", [("abc", 3), ("aaa", 6)])
def test_solution(solution, case, expected):
    assert solution.count_substrings(case) == expected
