class Solution:
    def climb_stairs(self, n: int) -> int:
        """
        n = 1
        1

        n = 2
        1 + 1
        2

        n = 3
        1 + 1 + 1 (n=2 + 1)
        2 + 1     (n=2 + 1)
        1 + 2     (n=1 + 2)

        n = 4
        1 + 1 + 1 + 1 (n=3 + 1)
        2 + 1 + 1     (n=3 + 1)
        1 + 2 + 1     (n=3 + 1)
        1 + 1 + 2     (n=2 + 2)
        2 + 2         (n=2 + 2)

        steps(i) = steps(i - 1) + steps(i - 2)
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        steps = [1, 2, 0]
        for i in range(2, n):
            steps[i % 3] = steps[(i - 1) % 3] + steps[(i - 2) % 3]
        return steps[(n - 1) % 3]

    def climbStairs_overwrite(self, n: int) -> int:
        steps = [1, 2]
        if n < 3:
            return steps[n - 1]
        for i in range(2, n):
            steps[i % 2] += steps[(i - 1) % 2]

        return steps[(n - 1) % 2]
