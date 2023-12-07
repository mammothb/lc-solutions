class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        def count_palindrome(s, i, j, n):
            while 0 <= i and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1

        n = len(s)
        result = ""
        count = 0
        for i in range(n):
            l_odd, r_odd = count_palindrome(s, i, i, n)
            l_even, r_even = count_palindrome(s, i, i + 1, n)
            len_odd = 0
            len_even = 0
            if l_odd <= r_odd:
                len_odd = r_odd - l_odd + 1
            if l_even <= r_even:
                len_even = r_even - l_even + 1

            if len_odd > len_even:
                if len_odd > count:
                    result = s[l_odd : r_odd + 1]
                    count = len_odd
            else:
                if len_even > count:
                    result = s[l_even : r_even + 1]
                    count = len_even

        return result
