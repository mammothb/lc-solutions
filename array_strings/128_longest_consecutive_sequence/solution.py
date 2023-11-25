from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        def find(parent, i):
            if parent[i] != i:
                # Optimize with path compression
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, size, i, j):
            i_rep = find(parent, i)
            j_rep = find(parent, j)
            if i_rep == j_rep:
                return
            # Union by size, optimizing to avoid O(n) chains is not strictly
            # necessary, but maintaining size is useful for the problem
            if size[i_rep] < size[j_rep]:
                i_rep, j_rep = j_rep, i_rep
            parent[i_rep] = j_rep
            size[j_rep] += size[i_rep]

        # Edge case
        if not nums:
            return 0

        parent = {}
        size = {}
        for num in nums:
            parent[num] = num
            size[num] = 1
        for num in parent:
            if num - 1 in parent:
                union(parent, size, num - 1, num)
            if num + 1 in parent:
                union(parent, size, num, num + 1)
        return max(size.values())

    def longest_consecutive_set(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        for num in nums_set:
            # Check for start of a sequence
            if num - 1 not in nums_set:
                y = num + 1
                while y in nums_set:
                    y += 1
                count = max(count, y - num)
        return count


if __name__ == "__main__":
    sol = Solution()
    sol.longest_consecutive([100, 4, 200, 1, 3, 2])
