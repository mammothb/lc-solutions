from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        def get_sum(candidates, target, start, stop, result, curr):
            if target == 0:
                result.append(curr)
            if target < 0:
                return
            for i in range(start, stop):
                if target - candidates[i] < 0:
                    continue
                curr_copy = curr.copy()
                curr_copy.append(candidates[i])
                if target - candidates[i] == 0:
                    result.append(curr_copy)
                else:
                    get_sum(
                        candidates, target - candidates[i], i, stop, result, curr_copy
                    )

        result = []
        n = len(candidates)
        get_sum(candidates, target, 0, n, result, [])
        return result
