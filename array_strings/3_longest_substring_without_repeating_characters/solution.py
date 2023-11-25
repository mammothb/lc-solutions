class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        count = 0
        l = 0
        for r, c in enumerate(s):
            if c not in seen:
                count = max(count, r - l + 1)
            else:
                # c exist within the current window at seen[c]
                # shrink left side of window to the right of seen[c]
                if seen[c] >= l:
                    l = seen[c] + 1
                # c is not actually in the current window
                else:
                    count = max(count, r - l + 1)
            seen[c] = r
        return count
