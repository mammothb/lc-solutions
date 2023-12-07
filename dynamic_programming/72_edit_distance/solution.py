class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        if min(len1, len2) == 0:
            return max(len1, len2)
        costs = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            costs[i][0] = i
        for j in range(1, len2 + 1):
            costs[0][j] = j
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] != word2[j - 1]:
                    costs[i][j] = min(
                        min(costs[i - 1][j - 1], costs[i - 1][j]), costs[i][j - 1]
                    )
                    costs[i][j] += 1
                else:
                    costs[i][j] = costs[i - 1][j - 1]
        return costs[-1][-1]

    def minDistance_space_optimized(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        len1 = len(word1)
        len2 = len(word2)
        if min(len1, len2) == 0:
            return max(len1, len2)
        costs = [i + 1 for i in range(len2)]
        for i in range(len1):
            above_cost = i
            left_cost = i
            for j in range(len2):
                curr_cost = left_cost
                left_cost = costs[j]
                if word1[i] != word2[j]:
                    curr_cost = min(min(curr_cost, left_cost), above_cost)
                    curr_cost += 1
                costs[j] = curr_cost
                above_cost = curr_cost
        return curr_cost
