import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events)
        total_days = max(stop for _, stop in events)
        idx = 0
        n = len(events)
        result = 0
        stops = []
        for day in range(1, total_days + 1):
            # Add events that started
            while idx < n and events[idx][0] == day:
                heapq.heappush(stops, events[idx][1])
                idx += 1
            # Clean up expired events
            while stops and stops[0] < day:
                heapq.heappop(stops)
            # If there's any end days, the event has already started,
            # So we attend the one that ends the earliest
            if stops:
                heapq.heappop(stops)
                result += 1
        return result
