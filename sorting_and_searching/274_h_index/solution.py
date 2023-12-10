from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        for i, c in enumerate(citations):
            if c < i + 1:
                return i
        return len(citations)

    def hIndex_counting_sort(self, citations: List[int]) -> int:
        n = len(citations)
        # Modified counting array from counting sort where we cap it at
        # number of papers instead of max citations because even in
        # [10, 10], h-index is 2
        counts = [0] * (n + 1)
        for c in citations:
            counts[min(n, c)] += 1

        h_index = n
        count = counts[n]
        # h-index is when the cumulative count first exceeds/is equal the
        # h-index
        while h_index > count:
            h_index -= 1
            count += counts[h_index]
        return h_index
