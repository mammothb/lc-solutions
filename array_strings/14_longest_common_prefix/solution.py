from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_length = min(len(string) for string in strs)
        if min_length == 0:
            return ""

        result = []
        idx = 0
        run = True
        while run:
            if idx == min_length:
                break
            result.append(strs[0][idx])
            for string in strs:
                if string[idx] != result[-1]:
                    result.pop()
                    run = False
                    break
            idx += 1
        return "".join(result)
