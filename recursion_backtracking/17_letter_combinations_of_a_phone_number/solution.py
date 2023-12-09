import collections
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        queue = collections.deque([""])
        length = 0
        for d in digits:
            while queue and len(queue[0]) == length:
                prefix = queue.popleft()
                for c in digit_to_letter[d]:
                    queue.append(f"{prefix}{c}")
            length += 1
        return list(queue)

    def letterCombinations_recursion(self, digits: str) -> List[str]:
        def solve(start, n, digits, digit_to_letter, curr, result):
            if start == n:
                result.append(curr)
                return
            for c in digit_to_letter[digits[start]]:
                solve(start + 1, n, digits, digit_to_letter, curr + c, result)

        if len(digits) == 0:
            return []

        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        solve(0, len(digits), digits, digit_to_letter, "", result)
        return result
