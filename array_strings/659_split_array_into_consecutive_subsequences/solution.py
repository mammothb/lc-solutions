import collections
import heapq
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Implicity Python's tuple comparison which compares all elements
        # Order by (num, count)
        # Keep appending to the shortest subsequence if possible
        h = []
        for num in nums:
            # No chance of appending to any previous subsequences
            while h and num > h[0][0] + 1:
                _, count = heapq.heappop(h)
                if count < 3:
                    return False
            if h and num == h[0][0] + 1:
                _, count = heapq.heappop(h)
                heapq.heappush(h, (num, count + 1))
            else:  # Reached when num == h[0][0], start a new subsequence
                heapq.heappush(h, (num, 1))
        while h:
            if heapq.heappop(h)[1] < 3:
                return False
        return True

    def isPossible_hashtable(self, nums: List[int]) -> bool:
        # number -> frequency
        counter = collections.Counter(nums)
        # last number in subsequence -> number of such subsequences
        subsequence = collections.defaultdict(lambda: 0)
        for num in nums:
            if counter[num] == 0:
                continue
            counter[num] -= 1
            # Append to existing subsequence
            if subsequence[num - 1] > 0:
                subsequence[num - 1] -= 1
                subsequence[num] += 1
            # Create new valid subsequence if possible
            elif counter[num + 1] > 0 and counter[num + 2] > 0:
                counter[num + 1] -= 1
                counter[num + 2] -= 1
                subsequence[num + 2] += 1
            # impossible to satisfy conditions
            else:
                return False
        return True
