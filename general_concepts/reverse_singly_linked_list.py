class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = ""
        while self is not None:
            result += f"{self.val}->"
            self = self.next
        return result[:-2]


def reverse_list(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


if __name__ == "__main__":
    head = None
    for i in reversed(range(1, 6)):
        head = ListNode(i, head)
    print(head)
    rev_head = reverse_list(head)
    print(rev_head)
