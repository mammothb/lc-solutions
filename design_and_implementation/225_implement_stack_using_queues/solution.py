import collections


class MyStack:
    def __init__(self):
        self.queue = collections.deque([])

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            x = self.queue.popleft()
            self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


class MyStack2:
    """For a sequence of A, B, C, the following structure is created
    [C, [B, [A, None]]]
    """

    def __init__(self):
        self.queue = None

    def push(self, x: int) -> None:
        queue = collections.deque([x])
        queue.append(self.queue)
        self.queue = queue

    def pop(self) -> int:
        val = self.queue.popleft()
        self.queue = self.queue[0]
        return val

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return self.queue is None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
