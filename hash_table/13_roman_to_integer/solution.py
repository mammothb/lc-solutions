class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        n = len(s)
        result = roman[s[-1]]
        for i in range(n - 2, -1, -1):
            result += roman[s[i]]
            if s[i] == "I" and (s[i + 1] in ("V", "X")):
                result -= 2
            elif s[i] == "X" and (s[i + 1] in ("L", "C")):
                result -= 20
            elif s[i] == "C" and (s[i + 1] in ("D", "M")):
                result -= 200
        return result
