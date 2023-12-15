import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        h = []
        indices = {}
        for i in range(len(s)):
            if s[i] not in indices:
                indices[s[i]] = len(h)
                h.append([0, s[i]])
            h[indices[s[i]]][0] -= 1
        heapq.heapify(h)
        result = ""
        while h:
            count, c = heapq.heappop(h)
            result += c * -count
        return result

    def frequencySort_bucket_sort(self, s: str) -> str:
        n = len(s)
        buckets = [None] * (n + 1)
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        for c, count in counter.items():
            if buckets[count] is None:
                buckets[count] = [c]
            else:
                buckets[count].append(c)
        result = ""
        for i in range(n, 0, -1):
            if buckets[i] is None:
                continue
            for c in buckets[i]:
                result += c * i
        return result
