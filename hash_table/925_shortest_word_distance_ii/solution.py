import collections
from typing import List


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.indices = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.indices[word].append(i)

    """
    @param word1: word1
    @param word2: word2
    @return: the shortest distance between two words
    """

    def shortest(self, word1: str, word2: str) -> int:
        # write your code here
        result = float("inf")
        list1 = self.indices[word1]
        list2 = self.indices[word2]
        n1 = len(list1)
        n2 = len(list2)
        i1 = 0
        i2 = 0
        # pairwise comparison
        while i1 < n1 and i2 < n2:
            result = min(result, abs(list1[i1] - list2[i2]))
            if list1[i1] < list2[i2]:
                i1 += 1
            else:
                i2 += 1
        return result
