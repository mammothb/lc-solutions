class CustomStack:

    def __init__(self, maxSize: int):
        self.capacity = maxSize
        self.size = 0
        self.stack = []

    def push(self, x: int) -> None:
        if self.size == self.capacity:
            return
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.stack[i] += val


class CustomStack2:
    def __init__(self, maxSize: int):
        self.capacity = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) == self.capacity:
            return
        self.stack.append(x)
        self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        inc = self.inc.pop()
        if self.inc:
            self.inc[-1] += inc
        return self.stack.pop() + inc

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
