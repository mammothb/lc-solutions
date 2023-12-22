import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.size = len(w)
        self.prefix = [0] * self.size
        self.prefix[0] = w[0]
        for i in range(1, self.size):
            self.prefix[i] = self.prefix[i - 1] + w[i]
        print(self.prefix)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[-1])
        l = 0
        r = self.size - 1
        idx = -1
        while l <= r:
            mid = l + (r - l) // 2
            if self.prefix[mid] == target:
                idx = mid
                break
            if self.prefix[mid] < target:
                l = mid + 1
            else:
                idx = mid
                r = mid - 1
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution([1, 3])
# print(obj.pickIndex())
