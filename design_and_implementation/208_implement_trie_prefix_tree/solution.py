class Node:
    def __init__(self):
        self.children = {c: None for c in "abcdefghijklmnopqrstuvwxyz"}
        self.is_word = False

    def __getitem__(self, key):
        return self.children[key]

    def __setitem__(self, key, val):
        self.children[key] = val


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if curr[c] is None:
                curr[c] = Node()
            curr = curr[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if curr[c] is None:
                return False
            curr = curr[c]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if curr[c] is None:
                return False
            curr = curr[c]
        return True


class Trie2:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["$"] = None

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return "$" in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie2()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
