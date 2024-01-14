import collections
from typing import List


def get_partial_table(pattern):
    n = len(pattern)
    result = [0] * n
    for i in range(1, n):
        j = result[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = result[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        result[i] = j
    return result


def search(string, pattern):
    np = len(pattern)
    partial = get_partial_table(pattern)
    result = collections.deque()
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = partial[j - 1]
        if pattern[j] == string[i]:
            j += 1
        if j == np:
            result.append(i - j + 1)
            j = partial[j - 1]
    return result


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        result = []

        idx_a = search(s, a)
        idx_b = search(s, b)
        while idx_a and idx_b:
            while idx_b and idx_b[0] < idx_a[0] - k:
                idx_b.popleft()
            if idx_b and abs(idx_b[0] - idx_a[0]) <= k:
                result.append(idx_a[0])
            idx_a.popleft()
        return result
