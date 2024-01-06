from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        result = n
        parent = {}
        size = {}
        for i in range(n):
            parent[i] = i
            size[i] = 1
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and self.union(parent, size, i, j):
                    result -= 1
        return result

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, size, l, r):
        l_rep = self.find(parent, l)
        r_rep = self.find(parent, r)

        if l_rep == r_rep:
            return False

        if size[l_rep] < size[r_rep]:
            l_rep, r_rep = r_rep, l_rep
        parent[r_rep] = l_rep
        size[l_rep] += size[r_rep]
        return True

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        result = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                self.dfs(isConnected, visited, n, i)
                result += 1
        return result

    def dfs(self, isConnected, visited, n, i):
        for j in range(n):
            if not visited[j] and isConnected[i][j] == 1:
                visited[j] = True
                self.dfs(isConnected, visited, n, j)
