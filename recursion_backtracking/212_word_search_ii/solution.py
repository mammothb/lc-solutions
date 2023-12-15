from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:
            def __init__(self):
                self.keys = {}

            def insert(self, word):
                keys = self.keys
                for c in word:
                    if not c in keys:
                        keys[c] = {}
                    keys = keys[c]
                keys["$"] = word

            # def contains(self, word):
            #     keys = self.keys
            #     for c in word:
            #         if not c in keys:
            #             return False
            #         keys = keys[c]
            #     return keys.get("$", False)

            # def starts_with(self, prefix):
            #     keys = self.keys
            #     for c in word:
            #         if not c in keys:
            #             return False
            #         keys = keys[c]
            #     return True

            def remove(self, word):
                keys = self.keys
                stack = []
                for c in word:
                    stack.append((keys, c))
                    keys = keys[c]
                del keys["$"]
                while stack:
                    keys, c = stack.pop()
                    if not keys[c]:
                        del keys[c]

        def dfs(board, nr, nc, trie, keys, i, j, result):
            if not (0 <= i < nr and 0 <= j < nc):
                return
            if board[i][j] == "#":
                return
            if board[i][j] not in keys:
                return

            c = board[i][j]
            keys = keys[c]
            board[i][j] = "#"

            if keys.get("$", ""):
                result.append(keys["$"])
                # Speeds up 8000ms to 890ms
                trie.remove(keys["$"])

            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                dfs(board, nr, nc, trie, keys, ii, jj, result)
            board[i][j] = c

        trie = Trie()
        for word in words:
            trie.insert(word)

        nr = len(board)
        nc = len(board[0])
        result = []
        for i in range(nr):
            for j in range(nc):
                if not trie.keys:
                    return result
                dfs(board, nr, nc, trie, trie.keys, i, j, result)
        return result
