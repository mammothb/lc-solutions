class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


class MyQueue2:
    def __init__(self):
        self.in_list = []
        self.out_list = []

    def push(self, x: int) -> None:
        self.in_list.append(x)

    def pop(self) -> int:
        self._fill_out_list()
        return self.out_list.pop()

    def peek(self) -> int:
        self._fill_out_list()
        return self.out_list[-1]

    def empty(self) -> bool:
        return len(self.in_list) == 0 and len(self.out_list) == 0

    def _fill_out_list(self):
        if not self.out_list:
            while self.in_list:
                self.out_list.append(self.in_list.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
