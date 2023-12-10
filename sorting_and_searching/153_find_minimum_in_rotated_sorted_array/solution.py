from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # When it's a non-rotated array
        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]

    def findMin_2(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
