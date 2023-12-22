from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        diff = 0
        diff_to_index = {0: -1}
        for i, num in enumerate(nums):
            if num == 0:
                diff -= 1
            else:
                diff += 1
            if diff in diff_to_index:
                result = max(result, i - diff_to_index[diff])
            else:
                diff_to_index[diff] = i

        return result
