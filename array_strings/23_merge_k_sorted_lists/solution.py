import heapq
from typing import List, Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(self):
    curr = self
    result = ""
    while curr is not None:
        result += f"{curr.val}->"
        curr = curr.next
    return result[:-2]


ListNode.__str__ = print_list


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(node.val, i) for i, node in enumerate(lists) if node is not None]
        heapq.heapify(h)
        root = ListNode()
        tail = root
        while h:
            _, i = heapq.heappop(h)
            tail.next = lists[i]
            tail = tail.next
            lists[i] = lists[i].next
            if lists[i] is not None:
                heapq.heappush(h, (lists[i].val, i))
        return root.next

    def merge_k_lists_dac(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l_merged, r_merged = self.merge_k_lists_dac(
            lists[:mid]
        ), self.merge_k_lists_dac(lists[mid:])
        return self.merge(l_merged, r_merged)

    def merge(self, l, r):
        root = ListNode()
        tail = root
        while l is not None and r is not None:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        # either l or r has to be None, for the above while loop to exit
        if l is not None:
            tail.next = l
        if r is not None:
            tail.next = r
        return root.next


@pytest.mark.parametrize(
    "case,expected",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ],
)
def test_solution(case, expected):
    lists = []
    for linked_list in case:
        root = ListNode()
        for val in reversed(linked_list):
            node = ListNode(val, root.next)
            root.next = node

        lists.append(root.next)
    expected_root = ListNode()
    for val in reversed(expected):
        node = ListNode(val, expected_root.next)
        expected_root.next = node
    expected_root = expected_root.next

    solution = Solution()
    actual = solution.merge_k_lists(lists)

    while actual is not None and expected_root is not None:
        assert actual.val == expected_root.val
        actual = actual.next
        expected_root = expected_root.next
    assert actual is None and expected_root is None


@pytest.mark.parametrize(
    "case,expected",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ],
)
def test_solution_dac(case, expected):
    lists = []
    for linked_list in case:
        root = ListNode()
        for val in reversed(linked_list):
            node = ListNode(val, root.next)
            root.next = node

        lists.append(root.next)
    expected_root = ListNode()
    for val in reversed(expected):
        node = ListNode(val, expected_root.next)
        expected_root.next = node
    expected_root = expected_root.next

    solution = Solution()
    actual = solution.merge_k_lists_dac(lists)

    while actual is not None and expected_root is not None:
        assert actual.val == expected_root.val
        actual = actual.next
        expected_root = expected_root.next
    assert actual is None and expected_root is None
