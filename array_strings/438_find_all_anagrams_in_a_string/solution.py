import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        counter_p = collections.Counter(p)
        counter = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
        result = []
        for i in range(len(s)):
            counter[s[i]] += 1
            if i >= len_p:
                counter[s[i - len_p]] -= 1
            if all(counter[k] == v for k, v in counter_p.items()):
                result.append(i - len_p + 1)
        return result

    def findAnagrams_space_optimize(self, s: str, p: str) -> List[int]:
        n = len(p)
        counter = collections.Counter(p)
        result = []
        for i in range(len(s)):
            if s[i] in counter:
                counter[s[i]] -= 1
            if i >= n and s[i - n] in counter:
                counter[s[i - n]] += 1
            if all(v == 0 for v in counter.values()):
                result.append(i - n + 1)
        return result
