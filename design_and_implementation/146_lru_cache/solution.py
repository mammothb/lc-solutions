class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def insert_after(self, other):
        other.next = self.next
        self.next.prev = other
        self.next = other
        other.prev = self

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = None
        self.next = None


def connect(l_node, r_node):
    r_node.next = l_node.next
    r_node.prev = l_node
    r_node.next.prev = r_node
    l_node.next = r_node


def disconnect(node):
    node.prev.next = node.next
    node.next.prev = node.prev


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.map = {}
        self.capacity = capacity
        self.count = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        disconnect(self.map[key])
        connect(self.head, self.map[key])

        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            disconnect(self.map[key])
            connect(self.head, self.map[key])
        else:
            if self.count >= self.capacity:
                del_key = self.tail.prev.key
                disconnect(self.tail.prev)
                del self.map[del_key]
            else:
                self.count += 1
            node = Node(key, value)
            self.map[key] = node
            connect(self.head, node)


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.lookup = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.lookup:
            return -1
        self.lookup[key].remove()
        self.head.insert_after(self.lookup[key])
        return self.lookup[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].val = value
            self.lookup[key].remove()
            self.head.insert_after(self.lookup[key])
            return
        if self.size == self.capacity:
            del_key = self.tail.prev.key
            node = self.lookup.pop(del_key)
            node.remove()
        else:
            self.size += 1
        self.lookup[key] = Node(key, value)
        self.head.insert_after(self.lookup[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
