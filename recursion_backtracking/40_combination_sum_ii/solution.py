from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        self.solve(candidates, 0, len(candidates), target, [], result)
        return result

    def solve(self, candidates, start, stop, target, curr, result):
        if target == 0:
            result.append(curr)
            return
        if target < 0:
            return

        for i in range(start, stop):
            # Skip starting another subarray identical to the previous
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            curr.append(candidates[i])
            self.solve(
                candidates, i + 1, stop, target - candidates[i], curr.copy(), result
            )
            curr.pop()
