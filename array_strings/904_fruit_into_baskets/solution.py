import collections
from typing import Dict, List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0
        start = 0
        n = len(fruits)
        counter: Dict[int, int] = collections.Counter()
        for i in range(n):
            counter[fruits[i]] += 1
            while start < i:
                if len(counter) <= 2:
                    break
                counter[fruits[start]] -= 1
                if counter[fruits[start]] == 0:
                    del counter[fruits[start]]
                start += 1
            result = max(result, i - start + 1)
        return result
