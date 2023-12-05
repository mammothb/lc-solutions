import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        query_to_word = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                query = f"{word[:i]}*{word[i + 1 :]}"
                query_to_word[query].append(word)
        queue = collections.deque()
        for i in range(n):
            query = f"{beginWord[:i]}*{beginWord[i + 1 :]}"
            queue.append((query, beginWord, 1))
        seen = set()
        while queue:
            parent_query, parent_word, count = queue.popleft()
            seen.add(parent_word)
            if parent_query not in query_to_word:
                continue
            for word in query_to_word[parent_query]:
                if word == parent_word:
                    continue
                if word == endWord:
                    return count + 1
                for i in range(n):
                    query = f"{word[:i]}*{word[i + 1 :]}"
                    if query == parent_query:
                        continue
                    queue.append((query, word, count + 1))
        return 0
