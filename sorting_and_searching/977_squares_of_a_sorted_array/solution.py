from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos_i = 0
        while pos_i < n and nums[pos_i] < 0:
            pos_i += 1
        if pos_i == 0:
            return [num**2 for num in nums]
        if pos_i == n:
            return [nums[i] ** 2 for i in range(n - 1, -1, -1)]
        result = []
        neg_i = pos_i - 1
        while 0 <= neg_i and pos_i < n:
            neg_2 = nums[neg_i] ** 2
            pos_2 = nums[pos_i] ** 2
            if neg_2 < pos_2:
                result.append(neg_2)
                neg_i -= 1
            else:
                result.append(pos_2)
                pos_i += 1
        while 0 <= neg_i:
            result.append(nums[neg_i] ** 2)
            neg_i -= 1
        while pos_i < n:
            result.append(nums[pos_i] ** 2)
            pos_i += 1
        return result

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        result = [0] * n
        idx = n - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                result[idx] = nums[r] ** 2
                r -= 1
            else:
                result[idx] = nums[l] ** 2
                l += 1
            idx -= 1
        return result
