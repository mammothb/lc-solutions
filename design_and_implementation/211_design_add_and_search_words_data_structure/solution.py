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
            keys, i = stack.pop()
            if i == n:
                if keys.get("$", False):
                    return True
                continue
            if word[i] == ".":
                for key in keys:
                    if key != "$":
                        stack.append((keys[key], i + 1))
            else:
                if word[i] in keys:
                    stack.append((keys[word[i]], i + 1))
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

    def search_recursive_2(self, word: str) -> bool:
        def dfs(keys, word, n, i):
            if i == n:
                return keys.get("$", False)
            if word[i] == ".":
                return any(dfs(keys[key], word, n, i + 1) for key in keys if key != "$")
            if word[i] not in keys:
                return False
            return dfs(keys[word[i]], word, n, i + 1)

        return dfs(self.keys, word, len(word), 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
