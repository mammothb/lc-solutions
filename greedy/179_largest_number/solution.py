import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # We want "3" to be larger than "30", because 330 > 303
        def compare(x, y):
            if x == y:
                return 0
            if x + y > y + x:
                return 1
            return -1

        nums = [str(num) for num in nums]
        nums = sorted(nums, key=functools.cmp_to_key(compare), reverse=True)
        result = "".join(nums).lstrip("0")
        if not result:
            return "0"
        return result
