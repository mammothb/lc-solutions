import pytest


class Solution:
    def decode_string(self, s: str) -> str:
        num = ""
        txt = ""
        stack = []
        for c in s:
            if c.isdigit():
                num += c
            elif c == "[":
                stack.append((num, txt))
                num = ""
                txt = ""
            elif c == "]":
                prev_num, prev_string = stack.pop()
                txt = prev_string + int(prev_num) * txt
            else:
                txt += c
        return txt


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("ef2[abc]3[cd]ef", "efabcabccdcdcdef"),
    ],
)
def test_solution(solution, case, expected):
    actual = solution.decode_string(case)
    assert actual == expected
