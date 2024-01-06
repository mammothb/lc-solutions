import collections
from typing import List


class Trie:
    def __init__(self):
        self.keys = collections.defaultdict(Trie)
        self.suggestions = []

    def add_suggestion(self, word):
        if len(self.suggestions) < 3:
            self.suggestions.append(word)

    def insert(self, word):
        node = self
        for c in word:
            node.keys[c].add_suggestion(word)
            node = node.keys[c]


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        products = sorted(products)
        for product in products:
            trie.insert(product)

        result = []
        for c in searchWord:
            trie = trie.keys[c]
            result.append(trie.suggestions)

        return result
