from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = n - 1
        while 0 <= idx:
            if nums[idx] != 0:
                break
            idx -= 1
        swapped = True
        while swapped:
            swapped = False
            for i in range(idx):
                if nums[i] == 0:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
            idx -= 1

    def moveZeroes_2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = 0
        # Shift all non-zeros
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        # Fill the rest with zeros
        while idx < n:
            nums[idx] = 0
            idx += 1
