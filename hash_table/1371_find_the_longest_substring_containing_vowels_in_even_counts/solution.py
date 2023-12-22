class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        diff_to_index = {0: -1}
        vowel = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        curr = 0
        result = 0
        for i, c in enumerate(s):
            if c in vowel:
                curr ^= vowel[c]
            if curr in diff_to_index:
                result = max(result, i - diff_to_index[curr])
            else:
                diff_to_index[curr] = i
        return result
