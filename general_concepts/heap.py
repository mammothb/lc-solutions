import sys
from typing import Any, Generic, List, Tuple, TypeVar

T = TypeVar("T")


class MaxHeap(Generic[T]):
    ROOT = 1

    def __init__(self) -> None:
        self.size = 0
        self.heap: List[Tuple[int, Any]] = [(sys.maxsize + 1, None)]

    def heapify(self):
        for i in reversed(range(1, int(self.size / 2) + 1)):
            self._sift_up(i)

    def push(self, item: Tuple[int, T]) -> None:
        self.heap.append(item)
        self.size += 1
        self._sift_down(self.ROOT, self.size)

    def _parent(self, pos: int) -> int:
        return int(pos / 2)

    def _l_child(self, pos: int) -> int:
        return pos * 2

    def _r_child(self, pos: int) -> int:
        return pos * 2 + 1

    def _sift_down(self, start: int, pos: int) -> None:
        new_item = self.heap[pos]
        while pos > start:
            parent_pos = self._parent(pos)
            # If new_item is bigger than parent, move parent to pos or the
            # previous parent's pos
            if new_item > (parent := self.heap[parent_pos]):
                self.heap[pos] = parent
                pos = parent_pos
                continue
            # Found the pos where new_item isn't bigger than the parent
            break
        self.heap[pos] = new_item

    def _sift_up(self, pos: int) -> None:
        start = pos
        new_item = self.heap[pos]
        child_pos = self._l_child(pos)
        while child_pos <= self.size:
            r_child_pos = self._r_child(pos)
            if (
                r_child_pos <= self.size
                and self.heap[r_child_pos] > self.heap[child_pos]
            ):
                child_pos = r_child_pos
            self.heap[pos] = self.heap[child_pos]
            pos = child_pos
            child_pos = self._l_child(pos)
        self.heap[pos] = new_item
        self._sift_down(start, pos)


class MinHeap(Generic[T]):
    ROOT = 1

    def __init__(self) -> None:
        self.size = 0
        self.heap: List[Tuple[int, Any]] = [(-sys.maxsize - 1, None)]

    def heapify(self):
        for i in reversed(range(1, int(self.size / 2) + 1)):
            self._sift_up(i)

    def push(self, item: Tuple[int, T]) -> None:
        self.heap.append(item)
        self.size += 1
        self._sift_down(self.ROOT, self.size)

    def _parent(self, pos: int) -> int:
        return int(pos / 2)

    def _l_child(self, pos: int) -> int:
        return pos * 2

    def _r_child(self, pos: int) -> int:
        return pos * 2 + 1

    def _sift_down(self, start: int, pos: int) -> None:
        new_item = self.heap[pos]
        while pos > start:
            parent_pos = self._parent(pos)
            # If new_item is bigger than parent, move parent to pos or the
            # previous parent's pos
            if new_item < (parent := self.heap[parent_pos]):
                self.heap[pos] = parent
                pos = parent_pos
                continue
            # Found the pos where new_item isn't bigger than the parent
            break
        self.heap[pos] = new_item

    def _sift_up(self, pos: int) -> None:
        start = pos
        new_item = self.heap[pos]
        child_pos = self._l_child(pos)
        while child_pos <= self.size:
            r_child_pos = self._r_child(pos)
            if (
                r_child_pos <= self.size
                and self.heap[r_child_pos] < self.heap[child_pos]
            ):
                child_pos = r_child_pos
            self.heap[pos] = self.heap[child_pos]
            pos = child_pos
            child_pos = self._l_child(pos)
        self.heap[pos] = new_item
        self._sift_down(start, pos)
