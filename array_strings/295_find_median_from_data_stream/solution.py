import heapq


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        if len(self.large) == 0:
            heapq.heappush(self.large, num)
        else:
            if num >= self.find_median():
                heapq.heappush(self.large, num)
                while len(self.large) - len(self.small) > 1:
                    heapq.heappush(self.small, -heapq.heappop(self.large))
            else:
                heapq.heappush(self.small, -num)
                while len(self.large) - len(self.small) < 0:
                    heapq.heappush(self.large, -heapq.heappop(self.small))

    def add_num_optimized(self, num: int) -> None:
        # Using .heappushpop(), we maintain length different <= 1
        # Keep `large` heap bigger
        if len(self.small) == len(self.large):
            # Add to `small` and then move the largest element from `small` to `large`
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def find_median(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 1:
            return self.large[0]
        return (self.large[0] - self.small[0]) / 2
