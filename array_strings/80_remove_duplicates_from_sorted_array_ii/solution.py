from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        indices = set()
        n = len(nums)
        for i in range(2, n):
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                indices.add(i)
        write_idx = 0
        read_idx = 0
        while read_idx < n:
            if read_idx not in indices:
                nums[write_idx] = nums[read_idx]
                write_idx += 1
            read_idx += 1
        return n - len(indices)
