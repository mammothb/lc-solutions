import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def is_less_than(word1, word2):
            len1 = len(word1)
            len2 = len(word2)
            idx1 = 0
            idx2 = 0
            while idx1 < len1 and idx2 < len2 and word1[idx1] == word2[idx2]:
                idx1 += 1
                idx2 += 1
            if idx1 == len1 and idx2 == len2:
                return False
            if idx1 == len1:
                return True
            if idx2 == len2:
                return False
            return word1[idx1] < word2[idx2]

        def lexico_sort(array):
            for i in range(1, len(array)):
                j = i
                tmp = array[i]
                while j > 0 and is_less_than(tmp, array[j - 1]):
                    array[j] = array[j - 1]
                    j -= 1
                array[j] = tmp

        n = len(words)
        buckets = [[] for _ in range(n + 1)]
        counter = collections.Counter(words)
        for word, count in counter.items():
            buckets[count].append(word)
        result = []
        for i in range(n, 0, -1):
            lexico_sort(buckets[i])
            for word in buckets[i]:
                result.append(word)
                if len(result) == k:
                    return result

    def topKFrequent_heap(self, words: List[str], k: int) -> List[str]:
        def is_less_than(word1, word2):
            len1 = len(word1)
            len2 = len(word2)
            idx1 = 0
            idx2 = 0
            while idx1 < len1 and idx2 < len2 and word1[idx1] == word2[idx2]:
                idx1 += 1
                idx2 += 1
            if idx1 == len1 and idx2 == len2:
                return False
            if idx1 == len1:
                return True
            if idx2 == len2:
                return False
            return word1[idx1] < word2[idx2]

        class Element:
            def __init__(self, word, count):
                self.word = word
                self.count = count

            def __lt__(self, other):
                if self.count != other.count:
                    return self.count < other.count
                return not is_less_than(self.word, other.word)

        counter = collections.Counter(words)
        # Min heap, so we pop smallest count or lexicographically later elements
        # and then reverse the result
        h = []
        for word, count in counter.items():
            heapq.heappush(h, Element(word, count))
            if len(h) > k:
                heapq.heappop(h)
        result = []
        while h:
            result.append(heapq.heappop(h).word)
        return reversed(result)
