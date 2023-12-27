from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]

        result = []
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if is_palindrome(f"{words[i]}{words[j]}"):
                    result.append([i, j])
                if is_palindrome(f"{words[j]}{words[i]}"):
                    result.append([j, i])
        return result

    def palindromePairs_hash_table(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return not word or word == word[::-1]

        word_map = {word: i for i, word in enumerate(words)}

        result = []
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                part1 = word[:j]
                part2 = word[j:]
                if is_palindrome(part1):
                    index = word_map.get(part2[::-1], None)
                    if index is not None and i != index:
                        result.append([index, i])
                if j < n and is_palindrome(part2):
                    index = word_map.get(part1[::-1], None)
                    if index is not None and i != index:
                        result.append([i, index])
        return result
