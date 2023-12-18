class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = x
        reverse = 0

        while tmp > 0:
            reverse = 10 * reverse + tmp % 10
            tmp //= 10
        return reverse == x
