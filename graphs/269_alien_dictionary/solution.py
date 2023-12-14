import collections
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


print(Solution().getAlienLanguage(["wrt", "wrf", "er", "ett", "rftt"]))
