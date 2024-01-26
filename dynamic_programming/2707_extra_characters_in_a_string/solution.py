from typing import List


class Trie:
    def __init__(self):
        self.keys = {}

    def insert(self, word):
        keys = self.keys
        for c in word:
            if c not in keys:
                keys[c] = {}
            keys = keys[c]
        keys["$"] = True

    def search(self, word):
        keys = self.keys
        for c in word:
            if c not in keys:
                return False
            keys = keys[c]
        return keys.get("$", False)


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        n = len(s)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for stop in range(n):
            dp[stop + 1] = dp[stop] + 1
            for start in range(stop, -1, -1):
                if trie.search(s[start : stop + 1]):
                    print(s[start : stop + 1])
                    dp[stop + 1] = min(dp[stop + 1], dp[start])
        return dp[-1]


print(Solution().minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"]))
