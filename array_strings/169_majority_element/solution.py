from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            if counter[num] > n / 2:
                return num

    def majorityElement_constant_space(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        count = 0
        for i in range(n):
            if nums[i] == result:
                count += 1
            elif count == 0:
                count += 1
                result = nums[i]
            else:
                count -= 1
        return result
