import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x > arr[-1]:
            return arr[-k:]
        if x < arr[0]:
            return arr[:k]
        n = len(arr)
        l = 0
        r = n - 1
        idx = -1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                idx = mid
                break
            if arr[mid] < x:
                l = mid + 1
            else:
                idx = mid
                r = mid - 1
        l = idx - 1
        r = idx
        h = []
        while 0 <= l and r < n:
            heapq.heappush(h, (-abs(arr[l] - x), -arr[l]))
            l -= 1
            while 0 <= l and arr[l] == arr[l + 1]:
                heapq.heappush(h, (-abs(arr[l] - x), -arr[l]))
                l -= 1
            heapq.heappush(h, (-abs(arr[r] - x), -arr[r]))
            r += 1
            while r < n and arr[r] == arr[r - 1]:
                heapq.heappush(h, (-abs(arr[r] - x), -arr[r]))
                r += 1
            while len(h) > k:
                heapq.heappop(h)
        result = [-elem[1] for elem in h]
        while len(result) < k and 0 <= l:
            result.append(arr[l])
            l -= 1
        while len(result) < k and r < n:
            result.append(arr[r])
            r += 1
        result.sort()
        return result

    def findClosestElements_2(self, arr: List[int], k: int, x: int) -> List[int]:
        if x > arr[-1]:
            return arr[-k:]
        if x < arr[0]:
            return arr[:k]
        n = len(arr)
        l = 0
        r = n - 1
        idx = -1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                idx = mid
                break
            if arr[mid] < x:
                l = mid + 1
            else:
                idx = mid
                r = mid - 1
        # Find the index nearest to x and restrict the search range to 2k
        l = max(0, idx - k)
        r = min(n, idx + k)
        h = []
        for i in range(l, r):
            heapq.heappush(h, (-abs(arr[i] - x), -arr[i]))
            if len(h) > k:
                heapq.heappop(h)
        result = sorted([-elem[1] for elem in h])
        return result

    def findClosestElements_binary_search(
        self, arr: List[int], k: int, x: int
    ) -> List[int]:
        if x > arr[-1]:
            return arr[-k:]
        if x < arr[0]:
            return arr[:k]
        n = len(arr)
        l = 0
        r = n - 1 - k
        while l <= r:
            mid = l + (r - l) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                r = mid - 1
            else:
                l = mid + 1

        return arr[l : l + k]
