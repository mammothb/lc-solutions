import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        indices = {}
        for num in nums:
            if num not in indices:
                indices[num] = len(h)
                h.append([0, num])
            h[indices[num]][0] -= 1
        heapq.heapify(h)
        result = [heapq.heappop(h)[1] for _ in range(k)]
        return result

    def topKFrequent_bucket_sort(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, count in counter.items():
            buckets[count].append(num)
        result = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
