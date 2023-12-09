from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            for j in range(i + 1, min(n, i + 1 + nums[i])):
                if dp[j] == 0:
                    dp[j] = dp[i] + 1
                else:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

    def jump_bfs(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        max_reachable = 0
        last_jump_pos = 0
        count = 0
        while last_jump_pos < n - 1:
            max_reachable = max(max_reachable, i + nums[i])
            if i == last_jump_pos:
                last_jump_pos = max_reachable
                count += 1
            i += 1
        return count

    def jump_bfs_2(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        count = 0
        pos = 0
        next_pos = 0
        i = pos
        # while we have not reached the end
        while pos < n - 1:
            count += 1
            # Find the max reachable position from the previous step's range
            while i <= pos:
                next_pos = max(next_pos, nums[i] + i)
                i += 1
            # Move to the max reachable within the current step
            pos = next_pos
        return count
