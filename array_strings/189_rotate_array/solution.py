from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return

        result = []
        for i in range(n):
            result.append(nums[(i - k) % n])
        for i in range(n):
            nums[i] = result[i]

    def rotate_constant_space(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, stop):
            while start < stop:
                nums[start], nums[stop] = nums[stop], nums[start]
                start += 1
                stop -= 1

        n = len(nums)
        k %= n
        if k == 0:
            return

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
