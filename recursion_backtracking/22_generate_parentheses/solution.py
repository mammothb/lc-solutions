from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(l, r, curr, result):
            if l == 0 and r == 0:
                result.append(curr)
                return
            if l > 0:
                solve(l - 1, r + 1, f"{curr}(", result)
            if r > 0:
                solve(l, r - 1, f"{curr})", result)

        result = []
        solve(n, 0, "", result)
        return result
