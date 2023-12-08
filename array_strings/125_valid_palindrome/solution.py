class Solution:
    def isPalindrome(self, s: str) -> bool:
        def solve(s, i, j, n):
            while 0 <= i and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return i == -1 and j == n

        s = "".join(c.lower() for c in s if c.isalnum())
        n = len(s)
        if n <= 1:
            return True
        m = n // 2
        return solve(s, m, m, n) or solve(s, m - 1, m, n)

    def isPalindrome2(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True
