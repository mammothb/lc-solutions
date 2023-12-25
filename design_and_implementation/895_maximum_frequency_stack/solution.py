import collections


class FreqStack:
    def __init__(self):
        self.freq = {}
        self.freq_to_stack = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1

        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]

        if self.freq[val] in self.freq_to_stack:
            self.freq_to_stack[self.freq[val]].append(val)
        else:
            self.freq_to_stack[self.freq[val]] = [val]

    def pop(self) -> int:
        val = self.freq_to_stack[self.max_freq].pop()

        if not self.freq_to_stack[self.max_freq]:
            self.max_freq -= 1
        self.freq[val] -= 1
        return val


class FreqStack2:
    def __init__(self):
        self.freq = collections.defaultdict(int)
        self.freq_to_stack = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.freq_to_stack[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.freq_to_stack[self.max_freq].pop()

        if not self.freq_to_stack[self.max_freq]:
            self.max_freq -= 1
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
