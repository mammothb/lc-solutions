from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key=lambda x: (-x[0], x[1]))
        result = 0
        max_def = float("-inf")
        for p in properties:
            if p[1] < max_def:
                result += 1
            max_def = max(max_def, p[1])
        return result
