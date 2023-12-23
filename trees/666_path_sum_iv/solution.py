import collections
from typing import List


class Solution:
    def path_sum_i_v(self, nums: List[int]) -> int:
        """
        @param nums: the list
        @return: the sum of all paths from the root towards the leaves
        """

        def dfs(dp, curr, dp_to_val, res):
            if dp not in dp_to_val:
                return
            curr += dp_to_val[dp]
            depth = dp // 10
            position = dp % 10
            left = (depth + 1) * 10 + (position * 2) - 1
            right = left + 1
            if left not in dp_to_val and right not in dp_to_val:
                res[0] += curr
                return
            dfs(left, curr, dp_to_val, res)
            dfs(right, curr, dp_to_val, res)

        res = [0]
        # Map <depth><position>: <value>
        dp_to_val = {num // 10: num % 10 for num in nums}
        dfs(11, 0, dp_to_val, res)
        return res[0]
