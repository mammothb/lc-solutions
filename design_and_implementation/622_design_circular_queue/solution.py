class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


#  class MyCircularQueue:
#      def __init__(self, k: int):
#          self.write_ptr = ListNode()
#          self.tail_ptr = self.write_ptr
#          for _ in range(k - 1):
#              self.write_ptr = ListNode(next=self.write_ptr)
#          self.tail_ptr.next = self.write_ptr
#          self.read_ptr = self.write_ptr
#
#      def enQueue(self, value: int) -> bool:
#          if self.write_ptr.val is not None:
#              return False
#          self.tail_ptr = self.write_ptr
#          self.write_ptr.val = value
#          self.write_ptr = self.write_ptr.next
#          return True
#
#      def deQueue(self) -> bool:
#          self.read_ptr.val = None
#          self.read_ptr = self.read_ptr.next
#          return True
#
#      def Front(self) -> int:
#          if self.read_ptr.val is None:
#              return -1
#          return self.read_ptr.val
#
#      def Rear(self) -> int:
#          if self.tail_ptr.val is None:
#              return -1
#          return self.tail_ptr.val
#
#      def isEmpty(self) -> bool:
#          return self.tail_ptr.val is None
#
#      def isFull(self) -> bool:
#          return self.write_ptr == self.read_ptr and self.read_ptr.val is not None


class MyCircularQueueStack:
    def __init__(self, k: int):
        self.capacity = k
        self.data = [None] * k
        self.write_ptr = 0
        self.read_ptr = 0
        self.tail_ptr = 0

    def enQueue(self, value: int) -> bool:
        if self.data[self.write_ptr] is not None:
            return False
        self.tail_ptr = self.write_ptr
        self.write_ptr = (self.write_ptr + 1) % self.capacity
        self.data[self.write_ptr] = value
        return True

    def deQueue(self) -> bool:
        if self.data[self.read_ptr] is None:
            return False
        self.data[self.read_ptr] = None
        self.read_ptr = (self.read_ptr + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.data[self.read_ptr] is None:
            return -1
        return self.data[self.read_ptr]

    def Rear(self) -> int:
        if self.data[self.tail_ptr] is None:
            return -1
        return self.data[self.tail_ptr]

    def isEmpty(self) -> bool:
        return self.data[self.read_ptr] is None

    def isFull(self) -> bool:
        return self.data[self.write_ptr] is not None
