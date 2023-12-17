class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ia = len(a) - 1
        ib = len(b) - 1
        result = ""
        carry = False
        while 0 <= ia and 0 <= ib:
            if a[ia] == "1" and b[ib] == "1":
                if carry:
                    result += "1"
                else:
                    result += "0"
                carry = True
            elif a[ia] == "1" or b[ib] == "1":
                if carry:
                    result += "0"
                    carry = True
                else:
                    result += "1"
                    carry = False
            else:
                if carry:
                    result += "1"
                else:
                    result += "0"
                carry = False
            ia -= 1
            ib -= 1
        while 0 <= ia:
            if a[ia] == "1":
                if carry:
                    result += "0"
                    carry = True
                else:
                    result += "1"
                    carry = False
            else:
                if carry:
                    result += "1"
                else:
                    result += "0"
                carry = False
            ia -= 1
        while 0 <= ib:
            if b[ib] == "1":
                if carry:
                    result += "0"
                    carry = True
                else:
                    result += "1"
                    carry = False
            else:
                if carry:
                    result += "1"
                else:
                    result += "0"
                carry = False
            ib -= 1
        if carry:
            result += "1"
        return result[::-1]

    def addBinary_cast_to_list(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry = 0
        result = []
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result.append(str(carry % 2))
            carry //= 2
        return "".join(reversed(result))
