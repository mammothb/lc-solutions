from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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

        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for stop in range(1, n + 1):
            for start in range(stop, -1, -1):
                if dp[start] and trie.search(s[start:stop]):
                    dp[stop] = True
                    break
        return dp[-1]

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        wordDict = set(wordDict)
        for stop in range(1, n + 1):
            for start in range(stop, -1, -1):
                if dp[start] and s[start:stop] in wordDict:
                    dp[stop] = True
                    break
        return dp[n]


#  print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(Solution().wordBreak(s="aaaaaaa", wordDict=["aaaa", "aaa"]))
