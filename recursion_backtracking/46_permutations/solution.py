from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_number(nums, length, result, curr):
            length -= 1
            if length == 0:
                result.append(curr + nums)
                return

            for i, num in enumerate(nums):
                get_number(nums[:i] + nums[i + 1 :], length, result, curr + [num])

        result = []
        get_number(nums, len(nums), result, [])
        return result

    def permute_2(self, nums: List[int]) -> List[List[int]]:
        def get_number(nums, visited, n, result, curr):
            if len(visited) == n:
                result.append(curr)
                return
            for num in nums:
                if num in visited:
                    continue
                visited.add(num)
                get_number(nums, visited, n, result, curr + [num])
                visited.remove(num)

        visited = set()
        result = []
        get_number(nums, visited, len(nums), result, [])
        return result

    def permute_3(self, nums: List[int]) -> List[List[int]]:
        def get_number(nums, start, n, result, curr):
            if start == n:
                result.append(curr)
                return
            for i in range(start, n):
                # Swap used number to the start and then iterate from its right
                nums[start], nums[i] = nums[i], nums[start]
                get_number(nums, start + 1, n, result, curr + [nums[start]])
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        get_number(nums, 0, len(nums), result, [])
        return result
