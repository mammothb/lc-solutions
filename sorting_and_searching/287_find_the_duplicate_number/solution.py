from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = 0
        for num in nums:
            if (seen >> num) & 1 == 1:
                return num
            seen |= 1 << num

    def findDuplicate_hash_table(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

    def findDuplicate_slow_fast_pointer(self, nums: List[int]) -> int:
        """Same concept as find start of loop in linked list."""
        slow = nums[0]
        fast = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
