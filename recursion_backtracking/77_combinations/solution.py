from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(start, n, k, curr, result):
            if k == 0:
                result.append(curr)
                return
            for i in range(start, n + 1):
                solve(i + 1, n, k - 1, curr + [i], result)

        result = []
        solve(1, n, k, [], result)
        return result
