class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i_s = len(s) - 1
        i_t = len(t) - 1

        while True:
            bs = 0
            while 0 <= i_s and (bs > 0 or s[i_s] == "#"):
                if s[i_s] == "#":
                    bs += 1
                else:
                    bs -= 1
                i_s -= 1
            bs = 0
            while 0 <= i_t and (bs > 0 or t[i_t] == "#"):
                if t[i_t] == "#":
                    bs += 1
                else:
                    bs -= 1
                i_t -= 1

            if 0 <= i_s and 0 <= i_t and s[i_s] == t[i_t]:
                i_s -= 1
                i_t -= 1
            else:
                break

        return i_s < 0 and i_t < 0
