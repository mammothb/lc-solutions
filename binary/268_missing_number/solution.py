from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for num in nums:
            result |= 1 << num
        for i in range(1, n + 1):
            if result & (1 << i) == 0:
                return i
        return 0

    def missingNumber_one_loop(self, nums: List[int]) -> int:
        # a ^ b ^ b = a
        xor = len(nums)
        for i, num in enumerate(nums):
            xor = xor ^ i ^ num
        return xor
