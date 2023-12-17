class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l = 0
        r = x // 2
        while l <= r:
            mid = (l + r) // 2
            mid_2 = mid * mid
            if mid_2 == x:
                return mid
            if mid_2 < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
