from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        idx = 0
        for i in range(n):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1

        return idx
