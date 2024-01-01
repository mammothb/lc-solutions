import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        total_word_length = len(words) * word_length
        n = len(s)
        if n < total_word_length:
            return []

        result = []
        target_counter = collections.Counter(words)
        for i in range(n - total_word_length + 1):
            if self.contains(s, i, i + total_word_length, word_length, target_counter):
                result.append(i)
        return result

    def contains(self, s, start, stop, word_length, target_counter):
        counter = collections.defaultdict(int)
        for i in range(start, stop, word_length):
            word = s[i : i + word_length]
            if word not in target_counter:
                break
            counter[word] += 1
            if counter[word] > target_counter[word]:
                break
        return counter == target_counter

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        word_length = len(words[0])
        total_word_length = len(words) * word_length

        if n < total_word_length:
            return []

        target_counter = collections.Counter(words)
        result = []
        for i in range(word_length):
            queue = collections.deque()
            counter = target_counter.copy()
            for j in range(i, n - word_length + 1, word_length):
                word = s[j : j + word_length]
                if counter.get(word, 0) == 0:
                    if word not in target_counter:
                        queue = collections.deque()
                        counter = target_counter.copy()
                    else:
                        while queue:
                            first_word = queue.popleft()
                            if first_word == word:
                                queue.append(word)
                                break
                            counter[first_word] += 1
                else:
                    counter[word] -= 1
                    queue.append(word)
                    if sum(counter.values()) == 0:
                        result.append(j - total_word_length + word_length)
                        first_word = queue.popleft()
                        counter[first_word] += 1

        return result


print(
    Solution().findSubstring2(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
)
