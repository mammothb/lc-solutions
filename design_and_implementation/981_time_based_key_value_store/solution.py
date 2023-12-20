class TimeMap:
    def __init__(self):
        self.key_to_value = {}
        self.key_to_timestamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_to_value:
            self.key_to_value[key] = {}
            self.key_to_timestamp[key] = []

        self.key_to_value[key][timestamp] = value
        self.key_to_timestamp[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_to_value:
            return ""
        if timestamp in self.key_to_value[key]:
            return self.key_to_value[key][timestamp]
        if self.key_to_timestamp[key][-1] < timestamp:
            return self.key_to_value[key][self.key_to_timestamp[key][-1]]
        if self.key_to_timestamp[key][0] > timestamp:
            return ""
        l = 0
        r = len(self.key_to_timestamp[key]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.key_to_timestamp[key][mid] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return self.key_to_value[key][self.key_to_timestamp[key][r]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
