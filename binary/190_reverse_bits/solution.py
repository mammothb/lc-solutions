class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            if ((n >> i) & 1) == ((n >> (31 - i)) & 1):
                continue
            n ^= 1 << (31 - i)
            n ^= 1 << i
        return n
