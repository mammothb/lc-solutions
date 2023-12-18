class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            if ((n >> i) & 1) == ((n >> (31 - i)) & 1):
                continue
            n ^= 1 << (31 - i)
            n ^= 1 << i
        return n

    def reverseBits_2(self, n: int) -> int:
        for i in range(16):
            # Run only if the 2 bits differ
            if ((n >> i) & 1) ^ ((n >> (31 - i)) & 1) == 1:
                n ^= 1 << i
                n ^= 1 << (31 - i)
        return n
