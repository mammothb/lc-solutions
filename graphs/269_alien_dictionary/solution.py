import collections
import heapq
from typing import List


class Solution:
    def getAlienLanguage(self, dictionary: List[str]):
        # Write your code here.
        def first_different_letter(word1, word2):
            idx1 = 0
            idx2 = 0
            len1 = len(word1)
            len2 = len(word2)
            while idx1 < len1 and idx2 < len2 and word1[idx1] == word2[idx2]:
                idx1 += 1
                idx2 += 1
            if idx1 == len1 or idx2 == len2:
                return None, None
            return word1[idx1], word2[idx2]

        n = len(dictionary)
        graph = collections.defaultdict(list)
        indegree = {}
        for i in range(1, n):
            s, t = first_different_letter(dictionary[i - 1], dictionary[i])
            if s is not None:
                graph[s].append(t)
        for c1 in graph:
            if c1 not in indegree:
                indegree[c1] = 0
            for c2 in graph[c1]:
                if c2 in indegree:
                    indegree[c2] += 1
                else:
                    indegree[c2] = 1
        queue = collections.deque()
        result = []
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        while queue:
            c = queue.popleft()
            for next_c in graph[c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    queue.append(next_c)
            result.append(c)
        if len(result) != len(indegree):
            return ""
        return "".join(result)

    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        def first_different_letter(word1, word2):
            n1 = len(word1)
            n2 = len(word2)
            i1 = 0
            i2 = 0
            while i1 < n1 and i2 < n1 and words1[i1] == word2[i2]:
                i1 += 1
                i2 += 1
            if i1 < n1 and i2 < n2:
                return word1[i1], word2[i2]
            return None

        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        letters = set()
        n = len(words)
        for i in range(n - 1):
            res = first_different_letter(words[i], words[i + 1])
            if res is not None:
                a, b = res
                if b not in graph[a]:
                    indegree[b] += 1
                graph[a].add(b)
            else:
                # For the edge case of ["abc", "ab"] and the condition:
                # The dictionary is invalid, if string a is prefix of string b
                # and b is appear before a.
                if len(words[i]) > len(words[i + 1]):
                    return ""
        for word in words:
            for c in word:
                letters.add(c)

        queue = []
        for c in letters:
            if indegree[c] == 0:
                queue.append(c)
        # Use heap to store the queue for the condition:
        # There may be multiple valid order of letters, return the smallest
        # in normal lexicographical order.
        # Example, if z -> [c, b, a], visit the children in normal lexicographical
        # order: [a, b, c]
        heapq.heapify(queue)

        result = []
        while queue:
            n_queue = len(queue)
            for _ in range(n_queue):
                c = heapq.heappop(queue)
                result.append(c)
                for next_c in graph[c]:
                    indegree[next_c] -= 1
                    if indegree[next_c] == 0:
                        heapq.heappush(queue, next_c)
        if len(result) != len(indegree):
            return ""
        return "".join(result)


#  print(Solution().getAlienLanguage(["wrt", "wrf", "er", "ett", "rftt"]))
print(Solution().alien_order(["abc", "ab"]))
