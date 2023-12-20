class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0
        signed = False
        numeric = False
        for c in s:
            if c == " ":
                if numeric or signed:
                    break
                continue
            if c == "+" and not signed and not numeric:
                sign = 1
                signed = True
            elif c == "-" and not signed and not numeric:
                sign = -1
                signed = True
            elif c.isnumeric():
                num = num * 10 + int(c)
                numeric = True
            else:
                break
        return min(2**31 - 1, max(-(2**31), sign * num))

    def myAtoi_dfa(self, s: str) -> int:
        sign = 1
        num = 0
        state = 0

        for c in s:
            if state == 0:
                if c == " ":
                    continue
                if c in "+-":
                    state = 1
                    if c == "-":
                        sign = -1
                elif c.isdigit():
                    state = 2
                    num = num * 10 + int(c)
                else:
                    return 0
            elif state == 1:
                if c.isdigit():
                    state = 2
                    num = num * 10 + int(c)
                else:
                    return 0
            elif state == 2:
                if c.isdigit():
                    num = num * 10 + int(c)
                else:
                    break
        return max(-(2**31), min(2**31 - 1, sign * num))
