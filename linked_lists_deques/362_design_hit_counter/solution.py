import collections


class HitCounter:
    def __init__(self):
        # Write your code here.
        self.queue = collections.deque([])

    def hit(self, timestamp):
        # Write your code here .
        # Register a hit at this time stamp.
        if self.queue and self.queue[0][0] == timestamp:
            self.queue[0][1] += 1
        else:
            self.queue.append([timestamp, 1])

    def getHits(self, timestamp):
        # Write your code here.
        # Return an integer denoting the number of hits in last 5 minitues.
        while self.queue and self.queue[0][0] + 300 < timestamp:
            self.queue.popleft()
        result = 0
        for hit in self.queue:
            result += hit[1]
        return result


class HitCounter2:
    def __init__(self):
        # Write your code here.
        self.capacity = 300
        self.hits = [0] * self.capacity
        self.timestamps = [0] * self.capacity

    def hit(self, timestamp):
        # Write your code here .
        # Register a hit at this time stamp.
        idx = timestamp % self.capacity
        if self.timestamps[idx] == timestamp:
            self.hits[idx] += 1
        else:
            self.timestamps[idx] = timestamp
            self.hits[idx] = 1

    def getHits(self, timestamp):
        # Write your code here.
        # Return an integer denoting the number of hits in last 5 minitues.
        result = 0
        for i in range(self.capacity):
            if self.timestamps[i] + self.capacity >= timestamp:
                result += self.hits[i]
        return result
