class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz".upper()}
        n = len(s)
        result = 0
        max_count = 0
        start = 0
        for stop in range(n):
            count[s[stop]] += 1
            # Highest freq in the current window
            max_count = max(max_count, count[s[stop]])
            # Shrink left window because we need more than k replacement to
            # maintain it
            while stop - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1

            result = max(result, stop - start + 1)
        return result
