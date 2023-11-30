from typing import List, Optional


class TreeNode:
    def __init__(self, val):
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None
        self.val = val


def create_tree_from_list(array: List[Optional[int]]) -> Optional[TreeNode]:
    if not array:
        return None

    def build_tree(array: List[Optional[int]], index: int) -> Optional[TreeNode]:
        if index >= len(array) or array[index] is None:
            return None
        node = TreeNode(array[index])
        node.left = build_tree(array, 2 * index + 1)
        node.right = build_tree(array, 2 * index + 2)
        return node

    return build_tree(array, 0)


def print_tree(root: Optional[TreeNode], depth: int = 0) -> None:
    r"""Given a tree:
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
    Print:
            7
        3
            6
    1
            5
        2
            4
    """
    if root is None:
        return
    print_tree(root.right, depth + 1)
    print(f"{'    ' * depth}{root.val}")
    print_tree(root.left, depth + 1)


def inorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    def traverse(node, result):
        if node is None:
            return
        traverse(node.left, result)
        result.append(node.val)
        traverse(node.right, result)

    result: List[int] = []
    traverse(root, result)
    return result


def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    result = []
    stack = []
    while root is not None or stack:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result


def preorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    def traverse(node, result):
        if node is None:
            return
        result.append(node.val)
        traverse(node.left, result)
        traverse(node.right, result)

    result: List[int] = []
    traverse(root, result)
    return result


def preorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result


def postorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    def traverse(node, result):
        if node is None:
            return
        traverse(node.left, result)
        traverse(node.right, result)
        result.append(node.val)

    result = []
    traverse(root, result)
    return result


def postorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    result = []
    stack = []
    while root is not None or stack:
        while root is not None:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()
        # The current node has an unprocessed right child
        if root.right is not None and (stack and root.right == stack[-1]):
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            result.append(root.val)
            root = None
    return result


#  root = create_tree_from_list([0, 1, 2, 3, None, None, 6])
root = create_tree_from_list(list(range(1, 8)))
print_tree(root)
print(postorder_traversal_recursive(root))
print(postorder_traversal_iterative(root))
