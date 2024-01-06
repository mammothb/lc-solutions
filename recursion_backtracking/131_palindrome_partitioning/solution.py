from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}
        return self.solve(s, memo)

    def solve(self, s, memo):
        if not s:
            return [[]]
        if s in memo:
            return memo[s]

        result = []
        n = len(s)
        for i in range(1, n + 1):
            if self.is_palindrome(s[:i]):
                for suffix in self.partition(s[i:]):
                    result.append([s[:i]] + suffix)
        memo[s] = result
        return result

    def is_palindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.dfs(s, [])
        return self.result

    def dfs(self, s, curr):
        if not s:
            self.result.append(curr)
            return
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                curr.append(s[:i])
                self.dfs(s[i:], curr.copy())
                curr.pop()
