import random


class RandomizedSet:
    def __init__(self):
        self.indices = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        val_idx = self.indices[val]
        # Modify index of last element
        self.indices[self.data[-1]] = val_idx
        self.data[val_idx], self.data[-1] = self.data[-1], self.data[val_idx]
        self.data.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return self.data[int(random.random() * len(self.data))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
