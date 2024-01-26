from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        indices = {}
        result = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word1 == word2:
                if word1 in indices and word == word1:
                    result = min(result, i - indices[word1])
            else:
                if word1 in indices and word == word2:
                    result = min(result, i - indices[word1])
                elif word2 in indices and word == word1:
                    result = min(result, i - indices[word2])
            indices[word] = i
        return result
