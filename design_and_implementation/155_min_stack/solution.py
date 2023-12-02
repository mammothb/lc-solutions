class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins or val <= self.getMin():
            self.mins.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.getMin():
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


class MinStack2:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            curr_min = min(val, self.getMin())
        else:
            curr_min = val
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStack3:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or val <= self.getMin():
            self.mins.append((val, len(self.stack)))

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) < self.mins[-1][1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
