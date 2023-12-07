from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        counts = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in counts:
                result[counts[key]].append(string)
            else:
                counts[key] = len(result)
                result.append([string])
        return result
