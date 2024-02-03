from typing import List


class BIT:
    """0-index implementation."""

    def __init__(self, n):
        self.n = n
        self.data = [0] * self.n

    def add(self, i, val):
        while i < self.n:
            self.data[i] += val
            i |= i + 1

    def sum(self, i):
        result = 0
        while i >= 0:
            result += self.data[i]
            i = (i & (i + 1)) - 1
        return result

    @classmethod
    def from_array(cls, arr):
        n = len(arr)
        bit = cls(n)
        for i in range(n):
            bit.add(i, arr[i])

        return bit


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result

    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people = sorted(people, key=lambda x: (x[0], -x[1]))
        result = [None] * n
        for p in people:
            count = 0
            for j in range(n):
                if result[j] is None:
                    if count == p[1]:
                        result[j] = p
                        break
                    count += 1
        return result

    def reconstructQueue3(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        bit = BIT(n)
        for i in range(1, n):
            bit.add(i, 1)

        people = sorted(people, key=lambda x: (x[0], -x[1]))
        result = [None] * n

        for p in people:
            l = 0
            r = n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if bit.sum(mid) < p[1]:
                    l = mid + 1
                else:
                    r = mid - 1
            result[l] = p
            bit.add(l, -1)
        return result


print(Solution().reconstructQueue3([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
