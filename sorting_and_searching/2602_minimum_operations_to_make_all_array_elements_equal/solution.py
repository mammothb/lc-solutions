from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        result = []
        n = len(nums)
        nums = sorted(nums)
        prefix = nums.copy()
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        for q in queries:
            if q <= nums[0] or q >= nums[-1]:
                result.append(abs(prefix[-1] - q * n))
                continue
            l = 0
            r = n - 1
            index = 0
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == q:
                    index = mid
                    break
                if nums[mid] < q:
                    index = mid
                    l = mid + 1
                else:
                    r = mid - 1
            l_ops = q * (index + 1) - prefix[index]
            r_ops = prefix[-1] - prefix[index] - q * (n - 1 - index)
            result.append(l_ops + r_ops)
        return result
