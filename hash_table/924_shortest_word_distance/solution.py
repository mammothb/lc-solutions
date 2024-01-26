from typing import List


class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """

    def shortest_distance(self, words: List[str], word1: str, word2: str) -> int:
        # Write your code here
        indices = {}
        result = len(words)
        for i, word in enumerate(words):
            indices[word] = i
            if word1 in indices and word2 in indices:
                result = min(result, abs(indices[word1] - indices[word2]))
        return result
