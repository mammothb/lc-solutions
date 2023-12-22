class Solution:
    def reverse(self, x: int) -> int:
        int_32 = 2**31 - 1
        sign = -1 if x < 0 else 1
        result = 0
        x = abs(x)
        while x > 0:
            tens_diff = int_32 // 10 - result
            if (
                tens_diff < 0
                or (sign > 0 and tens_diff * 10 + int_32 % 10 < x % 10)
                # Add 1 more for negative
                or (sign < 0 and tens_diff * 10 + int_32 % 10 + 1 < x % 10)
            ):
                return 0
            result = 10 * result + x % 10
            x //= 10
        result *= sign
        return result
