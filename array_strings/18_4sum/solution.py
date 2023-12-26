from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def solve(nums, start, stop, target):
            result = []
            for i in range(start, stop - 2):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                l = i + 1
                r = stop - 1
                while l < r:
                    total = nums[i] + nums[l] + nums[r]
                    if total == target:
                        result.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
            return result

        nums = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            three_sum_result = solve(nums, i + 1, n, target - nums[i])
            for sub_result in three_sum_result:
                result.append([nums[i]] + sub_result)
        return result
