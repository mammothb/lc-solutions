from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [pivot] * n
        l = 0
        r = n - 1
        for i in range(n):
            if nums[i] < pivot:
                result[l] = nums[i]
                l += 1
            if nums[n - 1 - i] > pivot:
                result[r] = nums[n - 1 - i]
                r -= 1
            if l > r:
                break
        return result
