import collections


class Solution:
    def longest_palindrome(self, s: str) -> int:
        # if there is aaaCCC, aCCCa is a valid palindrome
        result = len(s)
        counter = collections.Counter(s)
        has_odd = False
        for count in counter.values():
            if count % 2 == 1:
                result -= 1
                has_odd = True
        return result + (1 if has_odd else 0)

    def longest_palindrome_set(self, s: str) -> int:
        # chars with even count will not be in the `char` set at the end
        char = set()
        for c in s:
            if c in char:
                char.remove(c)
            else:
                char.add(c)
        return len(s) - (max(0, len(char) - 1))
