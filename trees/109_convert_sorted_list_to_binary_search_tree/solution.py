from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_list_to_bst(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def build_tree(node, length):
            if length <= 0:
                return None
            i = 0
            mid = length // 2
            curr = node
            while i < mid:
                i += 1
                curr = curr.next
            root = TreeNode(curr.val)
            root.left = build_tree(node, mid)
            root.right = build_tree(curr.next, length - mid - 1)
            return root

        curr = head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next

        root = build_tree(head, length)
        return root

    def sorted_list_to_bst_two_pointer(
        self, head: Optional[ListNode]
    ) -> Optional[TreeNode]:
        def build_tree(head, tail):
            if head == tail:
                return None
            slow = head
            fast = head
            # Use the fact that when the fast pointer reaches the end
            # the slow pointer will be in the middle
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)
            root.left = build_tree(head, slow)
            root.right = build_tree(slow.next, tail)
            return root

        return build_tree(head, None)

    def sorted_list_to_bst_two_pointer_2(
        self, head: Optional[ListNode]
    ) -> Optional[TreeNode]:
        if head is None:
            return None
        # This is the last node in the list, return as a leaf node
        if head.next is None:
            return TreeNode(head.val)
        prev = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Cut the left side of the list
        prev.next = None
        root = TreeNode(slow.val)
        root.left = self.sorted_list_to_bst_two_pointer_2(head)
        root.right = self.sorted_list_to_bst_two_pointer_2(slow.next)
        return root
