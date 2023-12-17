class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while (b & mask) > 0:
            carry = a & b
            a ^= b
            b = carry << 1
        if b > 0:
            return a & mask
        return a
