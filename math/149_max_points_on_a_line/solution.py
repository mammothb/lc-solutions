import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            while b != 0:
                t = b
                b = a % b
                a = t
            return a

        n = len(points)
        if n < 3:
            return n

        result = 0
        for i in range(n):
            counter = collections.defaultdict(int)
            num_duplicate = 1
            for j in range(i + 1, n):
                # Avoid div by zero in grad calculation
                if points[j][0] == points[i][0] and points[j][1] == points[i][1]:
                    num_duplicate += 1
                else:
                    dx = points[j][0] - points[i][0]
                    dy = points[j][1] - points[i][1]
                    div = gcd(dx, dy)
                    dx //= div
                    dy //= div
                    # Avoid using float as keys
                    counter[(dx, dy)] += 1
            result = max(result, num_duplicate)
            for val in counter.values():
                result = max(result, val + num_duplicate)

        return result
