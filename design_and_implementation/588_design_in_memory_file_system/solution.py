from typing import List, Optional


class Trie:
    def __init__(self):
        self.name = None
        self.is_file = False
        self.content = []
        self.children = {}

    def insert(self, path: str, is_file: bool) -> "Trie":
        node = self
        parts = path.split("/")
        for part in parts[1:]:
            if part not in node.children:
                node.children[part] = Trie()
            node = node.children[part]
        if is_file:
            node.is_file = True
            node.name = parts[-1]

        return node

    def search(self, path: str) -> Optional["Trie"]:
        if path == "/":
            return self

        node = self
        parts = path.split("/")
        for part in parts[1:]:
            if part not in node.children:
                return None
            node = node.children[part]
        return node


class FileSystem:
    def __init__(self):
        self.root = Trie()

    def ls(self, path: str) -> List[str]:
        node = self.root.search(path)
        if node.is_file:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.root.insert(path, False)

    def addContentToFile(self, path: str, content: str) -> None:
        file = self.root.insert(path, True)
        file.content.append(content)

    def readContentFromFile(self, path: str) -> str:
        file = self.root.search(path)
        if file is not None and file.is_file:
            return "".join(file.content)
        return ""


fs = FileSystem()
print(fs.ls("/"))
fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d", "hello")
print(fs.ls("/"))
print(fs.readContentFromFile("/a/b/c/d"))
fs.addContentToFile("/a/b/c/d", "hello")
print(fs.readContentFromFile("/a/b/c/d"))
fs.mkdir("/v/b/c")
fs.mkdir("/b/b/c")
print(fs.ls("/"))
