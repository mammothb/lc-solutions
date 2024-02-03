class BIT:
    """0-index implementation."""

    def __init__(self, n):
        self.n = n
        self.data = [0] * self.n

    def add(self, i, val):
        while i < self.n:
            self.data[i] += val
            i |= i + 1

    def sum(self, i):
        result = 0
        while i >= 0:
            result += self.data[i]
            i = (i & (i + 1)) - 1
        return result

    @classmethod
    def from_array(cls, arr):
        n = len(arr)
        bit = cls(n)
        for i in range(n):
            bit.add(i, arr[i])

        return bit


class BIT2:
    """1-index implementation."""

    def __init__(self, n):
        self.n = n + 1
        self.data = [0] * self.n

    def add(self, i, val):
        while i < self.n:
            self.data[i] += val
            i += i & -i

    def sum(self, i):
        result = 0
        while i > 0:
            result += self.data[i]
            i -= i & -i
        return result

    @classmethod
    def from_array(cls, arr):
        n = len(arr)
        bit = cls(n)
        for i in range(n):
            bit.add(i + 1, arr[i])

        return bit


nums = [1, 2, 3, 4, 5, 6, 7]
bit = BIT.from_array(nums)
bit2 = BIT2.from_array(nums)
print(bit.data)
print(bit2.data)
print(bit.sum(5))
print(bit2.sum(6))
