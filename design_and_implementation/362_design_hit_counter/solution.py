import collections


class HitCounter:
    def __init__(self):
        # Write your code here.
        self.queue = collections.deque([])

    def hit(self, timestamp):
        # Write your code here .
        # Register a hit at this time stamp.
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])

    def getHits(self, timestamp):
        # Write your code here.
        # Return an integer denoting the number of hits in last 5 minitues.
        while self.queue and self.queue[0][0] + 300 <= timestamp:
            self.queue.popleft()
        result = 0
        for hit in self.queue:
            result += hit[1]
        return result


class HitCounter2:
    def __init__(self):
        self.capacity = 300
        self.hits = [0] * self.capacity
        self.timestamps = [0] * self.capacity

    def hit(self, timestamp: int):
        """
        @param timestamp: the timestamp
        @return: nothing
        """
        index = timestamp % self.capacity
        if self.timestamps[index] == timestamp:
            self.hits[index] += 1
        else:
            self.timestamps[index] = timestamp
            self.hits[index] = 1

    def getHits(self, timestamp: int) -> int:
        """
        @param timestamp: the timestamp
        @return: the count of hits in recent 300 seconds
        """
        return sum(
            self.hits[i]
            for i in range(self.capacity)
            if self.timestamps[i] + 300 > timestamp
        )
