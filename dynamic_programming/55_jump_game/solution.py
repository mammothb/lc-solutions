from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        # Start from last index
        dp[n - 1] = True
        idx = n - 2
        while idx >= 0:
            # Check if this can reach any of the next reachable nodes
            for i in range(idx + 1, min(n, idx + 1 + nums[idx])):
                if dp[i]:
                    dp[idx] = True
                    break
            idx -= 1
        return dp[0]

    def can_jump_2(self, nums: List[int]) -> bool:
        n = len(nums)
        to_reach = n - 1
        idx = n - 2
        while idx >= 0:
            # if current max distance can reach another reachable node, set
            # current as the next target
            if nums[idx] + idx >= to_reach:
                to_reach = idx
            idx -= 1
        return to_reach == 0

    def canJump_3(self, nums: List[int]) -> bool:
        n = len(nums)
        stop = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= stop:
                stop = i
        return stop == 0
