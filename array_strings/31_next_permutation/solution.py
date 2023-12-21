from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # From https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
        n = len(nums)
        small = -1
        # Find index such that nums[small + 1 :] is sorted in descending order
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                small = i
                break
        if small == -1:
            l = 0
            r = n - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        else:
            # Find the smallest element that's larger than nums[small],
            # since nums[small + 1 :] is sorted in descending order, start
            # from the right
            large = -1
            for i in range(n - 1, -1, -1):
                if nums[i] > nums[small]:
                    large = i
                    break
            nums[small], nums[large] = nums[large], nums[small]
            l = small + 1
            r = n - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
