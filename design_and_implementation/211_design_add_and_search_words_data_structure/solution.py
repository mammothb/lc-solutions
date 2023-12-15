class WordDictionary:
    def __init__(self):
        self.keys = {}

    def addWord(self, word: str) -> None:
        keys = self.keys
        for c in word:
            if c not in keys:
                keys[c] = {}
            keys = keys[c]
        keys["$"] = True

    def search(self, word: str) -> bool:
        n = len(word)
        stack = [(self.keys, 0)]
        while stack:
            keys, idx = stack.pop()
            if idx == n:
                if keys.get("$", False):
                    return True
            elif word[idx] == ".":
                for k in keys:
                    if k != "$":
                        stack.append((keys[k], idx + 1))
                continue
            else:
                if word[idx] in keys:
                    stack.append((keys[word[idx]], idx + 1))

        return False

    def search_recursive(self, word: str) -> bool:
        def dfs(word, n, i, keys):
            if i == n:
                return keys.get("$", False)
            if word[i] == ".":
                for k in keys:
                    if k != "$" and dfs(word, n, i + 1, keys[k]):
                        return True
            if word[i] in keys:
                return dfs(word, n, i + 1, keys[word[i]])
            return False

        return dfs(word, len(word), 0, self.keys)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
