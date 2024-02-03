class Solution:
    """Given an integer n, return the nth digit of the infinite integer sequence
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

      1-9   | 9
     10-99  | 90
    100-999 | 900
    """

    def findNthDigit(self, n: int) -> int:
        ndigit = 1
        base = 1
        # Find which digit range the nth digit is in
        while n > 9 * base * ndigit:
            n -= 9 * base * ndigit
            ndigit += 1
            base *= 10
        # Change to be 0-index.
        # Divide to find which number (offset from the start of the range) it is
        # r is the digit position in that number
        q, r = divmod(n - 1, ndigit)
        return int(str(base + q)[r])
