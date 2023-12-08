class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

    def disconnect(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = None
        self.next = None

    def insert_after(self, new_node):
        new_node.prev = self
        new_node.next = self.next
        self.next.prev = new_node
        self.next = new_node


class AllOne:
    """Doubly linked list to store counts and the keys with those counts.
    Uses a dict to map key to linked list nodes. Multiple keys may link to the
    same node.
    """

    def __init__(self):
        self.key_to_node = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if not key in self.key_to_node:
            node = self.head
        else:
            node = self.key_to_node[key]
            node.keys.remove(key)
        if node.count + 1 != node.next.count:
            new_node = Node(node.count + 1)
            node.insert_after(new_node)
        else:
            new_node = node.next
        new_node.keys.add(key)
        self.key_to_node[key] = new_node
        if node != self.head and not node.keys:
            node.disconnect()

    def dec(self, key: str) -> None:
        node = self.key_to_node[key]
        node.keys.remove(key)
        if node.count - 1 != node.prev.count:
            new_node = Node(node.count - 1)
            node.prev.insert_after(new_node)
        else:
            new_node = node.prev
        new_node.keys.add(key)
        self.key_to_node[key] = new_node
        if node != self.head and not node.keys:
            node.disconnect()

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        key = self.tail.prev.keys.pop()
        self.tail.prev.keys.add(key)
        return key

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        key = self.head.next.keys.pop()
        self.head.next.keys.add(key)
        return key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
